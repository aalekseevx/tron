let my_log;
let current_frame = 0;
let is_playing = 0;
let timer_id;
let n, m;
let frame_max;
let streams;

function settimer() {
    clearInterval(timer_id);
    if (is_playing) {
        let speed = $("#speed").val();
        timer_id = setInterval(to_next_frame, 100 - speed)
    }
}

function changeframe() {
    current_frame = $("#moment").val();
    redraw()
}
function setframerange() {
    $("#moment").val(current_frame)
}

function update() {
    if (is_playing) {
        settimer();
        $("#play_button").html("<i class=\"fas fa-pause\"></i>")
    } else {
        $("#play_button").html("<i class=\"fas fa-play\">");
        clearInterval(timer_id)
    }
}

function repeat() {
    current_frame = 0;
    is_playing = 0;
    update();
    redraw();
    setframerange()
}

$(document).ready(function() {
    let url = new URL(window.location.href);
    let id = url.searchParams.get("id");
    console.log("getting");
    $.getJSON("/challenge/log?id=" + id + "&format=json", function (data) {
        console.log(data);
        my_log = data;
        n = my_log[current_frame]["board"].length;
        m = my_log[current_frame]["board"][0].length;
        frame_max = my_log.length - 2;
        $("#moment").attr("max", frame_max);

        for(let i = 0; i < n; i++) {
            for (let j = 0; j < m; j++) {
                styles = 'style="height: ' + (100.0 / n).toString() + '%; width:' + (100.0 / m).toString() + '%"';
                $(".board").append('<div class="board_basic_cell" ' + styles + '><div id="cell_' + i.toString() + '_' + j.toString()+ '"></div></div>');
            }
        }

        $("#play_button").click(function () {
            is_playing ^= 1;
            update()
        });

        $("#repeat_button").click(repeat);

        $("#prev_button").click(to_previous_frame);
        $("#next_button").click(to_next_frame);
        // $("#field_id").text(data['challenge_id']);
        // $("#field_player1").text(data['player1']);
        // $("#field_player2").text(data['player2']);
        // $("#field_player1_verd").text(data['verdicts'][0]);
        // $("#field_player2_verd").text(data['verdicts'][1]);
        // $("#field_winner").text(data['winner']);

        console.log("getting streams");
        $.getJSON("/challenge/get_streams?id=" + id + "&streams[]=stdin&streams[]=stdout&streams[]=stderr&players[]=0&players[]=1", function (data) {
            console.log("got streams");
            streams = data;
            $.getJSON('/challenge/get_info?id=' + id, function (data) {
                $("#field_id").text(data['id']);
                $("#field_player1").text(data['player1']);
                $("#field_player2").text(data['player2']);
                $("#field_player1_verd").text(data['player1_verdict']);
                $("#field_player2_verd").text(data['player2_verdict']);
                $("#field_winner").text(data['winner']);

                //now we can display everything
                $("#root").attr("style", "display: auto");
                $(".loader").attr("style", "display: none");
                $("#download_stdin1").attr("href", "get_streams?id=" + id + "&streams[]=stdin&players[]=0");
                $("#download_stdout1").attr("href", "get_streams?id=" + id + "&streams[]=stdout&players[]=0");
                $("#download_stderr1").attr("href", "get_streams?id=" + id + "&streams[]=stderr&players[]=0");
                $("#download_stdin2").attr("href", "get_streams?id=" + id + "&streams[]=stdin&players[]=1");
                $("#download_stdout2").attr("href", "get_streams?id=" + id + "&streams[]=stdout&players[]=1");
                $("#download_stderr2").attr("href", "get_streams?id=" + id + "&streams[]=stderr&players[]=1");
                redraw()
            })
        });

        new ClipboardJS('.button');
    });
});

function str_for_html(str) {
    return $
}

function to_next_frame() {
    if (current_frame + 1 == my_log.length) {
        is_playing = 0;
        update();
        return;
    }
    current_frame++;
    redraw();
    setframerange()
}

function to_previous_frame() {
    current_frame = Math.max(0, current_frame - 1);
    redraw();
    setframerange()
}

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

function redraw() {
    class_mapper = {
        0: "empty",
        1: "red",
        2: "red_tail",
        3: "red_tail",
        4: "red_tail",
        5: "red_tail",
        6: "red_tail",
        7: "red_tail",
        8: "red_tail",
        9: "red_tail",
        10: "red_tail",
        11: "red_tail",
        12: "red_tail",
        13: "blue",
        14: "blue_tail",
        15: "blue_tail",
        16: "blue_tail",
        17: "blue_tail",
        18: "blue_tail",
        19: "blue_tail",
        20: "blue_tail",
        21: "blue_tail",
        22: "blue_tail",
        23: "blue_tail",
        24: "blue_tail",
        25: "block",
        26: "",
        27: "",
        28: "",
    };

    lit_mapper = {
        0: ".",
        1: "R",
        2: "Q",
        3: "Q",
        4: "Q",
        5: "Q",
        6: "Q",
        7: "Q",
        8: "Q",
        9: "Q",
        10: "Q",
        11: "Q",
        12: "Q",
        13: "B",
        14: "W",
        15: "W",
        16: "W",
        17: "W",
        18: "W",
        19: "W",
        20: "W",
        21: "W",
        22: "W",
        23: "W",
        24: "W",
        25: "X",
        26: "",
        27: "",
        28: "",
    };

    $("#player_board").html("");
    for(let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            let cur_id = my_log[current_frame]["board"][i][j];
            let cur_class = class_mapper[cur_id];
            let cur_lit = lit_mapper[cur_id];
            $("#cell_" + i + "_" + j).attr("class", "square " + cur_class);
        }
    }


    $("#points1").html(my_log[current_frame]["points"][0]);
    $("#points2").html(my_log[current_frame]["points"][1]);

    for (let player = 0; player < 2; player++) {
        $("#stdin" + (player + 1)).html(streams['stdin'][player][current_frame].replaceAll('\n', '<br>'));
        $("#stdout" + (player + 1)).html(streams['stdout'][player][current_frame]);
        $("#stderr" + (player + 1)).html(streams['stderr'][player][current_frame]);
    }
}


window.onkeydown = function (event) {
    let keyName = event.key;
    console.log(event.key);
    if (keyName.toString() == "ArrowRight") {
        to_next_frame();
    } else if (keyName.toString() == "ArrowLeft") {
        to_previous_frame();
    } else if (keyName == ' ') {
        is_playing ^= 1;
        update();
        event.preventDefault();
    } else if (event.which == 82) {
        console.log(event.key);
        repeat();
    }
};