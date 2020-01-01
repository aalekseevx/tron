#include <iostream>
#include <random>
#include <time.h>
using namespace std;

mt19937 rnd(time(0));

int level, n, m;
char my_ptr, enemy_ptr, enemy_tail;
vector < vector < char > > field;

int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};
char lit[] = {'U', 'R', 'D', 'L'};

int ddx[] = {0, 1, 1, 1, 0, -1, -1, -1};
int ddy[] = {-1, -1, 0, 1, 1, 1, 0, -1};

int my_x = -1, my_y = -1;
vector < int > pos;
bool touch = false;

int get_rnd(int r) {
    return abs(int(rnd())) % r;
}

void input() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> field[i][j];
            if (field[i][j] == my_ptr) {
                my_y = i;
                my_x = j;
            }
        }
    }
}

bool correct(int x, int y) {
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool check() {
    for (int i = 0; i < 8; ++i) {
        if (correct(my_x + ddx[i], my_y + ddy[i])) {
            if (field[my_y + ddy[i]][my_x + ddx[i]] == enemy_ptr ||
                field[my_y + ddy[i]][my_x + ddx[i]] == enemy_tail) {
                //cerr << "YASYA" << endl;
                return true;
            }
        }
    }
    return false;
}

bool dept(int x, int y, int d) {
    if (d <= 0)
        return true;

    if (field[y][x] == '.')
        field[y][x] = 'G';
    else
        return false;

    bool qans = false;
    for (int i = 0; i < 4; ++i) {
        if (correct(my_x + dx[i], my_y + dy[i])) {
            if (dept(my_x + dx[i], my_y + dy[i], d - 1))
                qans = true;
        }
    }

    field[y][x] = '.';
    return qans;
}

void make_move() {
    int ans;
    if(my_ptr == 'R')
        ans = 'R';
    else
        ans = 'L';

    input();


    if (!touch)
        touch = check();

    if (!touch) {
        if (my_ptr == 'R') {
            //cerr << my_x << " " << my_y << endl;
            //cerr << my_ptr << endl;
            if (my_x < my_y) {
                ans = 1;
            } else {
                ans = 2;
            }
        } else {
            if (my_x < my_y) {
                ans = 0;
            } else {
                ans = 3;
            }
        }
    }
    else {
        int ld = 0, cur;
        if (pos.size())
            ld = (pos[pos.size() - 1] + 2) % 4;
        for (int j = 0; j < 4; ++j) {
            cur = (ld + j) % 4;
            //cerr << cur << endl;
            if (correct(my_x + dx[cur], my_y + dy[cur]) &&
                field[my_y + dy[cur]][my_x + dx[cur]] == '.' &&
                dept(my_x + dx[cur], my_y + dy[cur], 2)) {
                ans = cur;
                //cerr << field[my_y + dy[cur]][my_x + dx[cur]] << endl;
                //cerr << cur << endl;
                break;
            }
        }
    }

    pos.push_back(ans);
    cout << lit[ans] << endl;
    cout.flush();
}

void INIT() {
    string player;
    cin >> player >> level >> n >> m;
    my_ptr = (player == "RED" ? 'R' : 'B');
    enemy_ptr = (player == "BLUE" ? 'R' : 'B');
    enemy_tail = (player == "BLUE" ? 'Q' : 'W');

    field.resize(n, vector < char > (m));
}

int main() {
    INIT();
    while(true) {
        make_move();
        //break;
    }
}