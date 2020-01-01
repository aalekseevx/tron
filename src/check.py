import os
from pathlib import Path
import json
import argparse
from loguru import logger
from select import select
from copy import deepcopy
import sys

problem_folder = Path(os.path.realpath(__file__)).parent.parent
lib_folder = os.path.join(problem_folder, 'lib')
sys.path.append(lib_folder)

from state import *
from sandbox import Sandbox


def parse_args():
    parser = argparse.ArgumentParser(prog='Tron checker', description='Perform fight for multiple players.')
    parser.add_argument('--players_cmd', metavar='CMD', nargs='+', required=True, type=str, help='A way to call each player.')
    parser.add_argument('--players_file', metavar='FILE', nargs='+', required=True, type=str, help='Players\' filename')
    parser.add_argument('--test_file', metavar='FILE', type=str, required=True, help='Test file.')
   
    parser.add_argument('--time_limit', metavar='SECS', default=1000, type=int, help='Time limit per move in microseconds')
    parser.add_argument('--memory_limit', metavar='BYTES', default=268435456, type=int, help='Memory limit per player in bytes')

    parser.add_argument('--streams_log_file', metavar='FILE', nargs=1, default='logs/streams.json', type=str, help='Output streams log file.')
    parser.add_argument('--checker_log_file', metavar='FILE', nargs=1, default='logs/checker.log', type=str, help='Output checker log file.')
    parser.add_argument('--game_log_file', metavar='FILE', nargs=1, default='logs/game.json', type=str, help='Output game log file.')
    parser.add_argument('--result_log_file', metavar='FILE', nargs=1, default='logs/result.json', type=str, help='Output result log file.')

    args = parser.parse_args()
    if len(args.players_cmd) != len(args.players_file):
        raise argparse.ArgumentTypeError("Players' cmds and files number are not equal.")
    return args

def start_player(data):
    return Sandbox.run(data[0], data[1])

def run_test(args, streams_log_file, game_log_file, result_log_file):
    logger.debug("Starting tests...")
    logger.debug(list(zip(args.players_cmd, args.players_file)))
    logger.debug(os.getcwd())

    with open(args.test_file) as test_file:
        state = State(test_file)
    iteration_number = 0
    players = [start_player(player) for player in zip(args.players_cmd, args.players_file)]

    streams_log = [{
        'stdin': [],
        'stdout': [],
        'stderr': []
    } for _ in range(len(players))]

    result_log = {
        'winner': None,
        'verdicts': ['OK' for _ in range(len(players))],
    }

    game_log = []

    float_timeout = float(args.time_limit) / 1000.0

    while not state.game_over:
        iteration_number += 1
        logger.debug(f'#Starting iteration {iteration_number}')
        player = players[state.get_current_player()]
        if player.poll() is not None:
            result_log['verdicts'][state.get_current_player()] = 'RE'
            state.ban_current_player()
            message = f'Process unexpectedly terminated with an exit code {player.poll()}.'
            for stream in ('stdin', 'stdout', 'stderr'):
                streams_log[state.get_current_player()][stream].append(message)
            continue

        current_stdin = state.get_input()

        pipes = select([], [player.stdin], [], float_timeout)[1]
        if player.stdin not in pipes:
            result_log['verdicts'][state.get_current_player()] = 'TL'
            state.ban_current_player()
            continue

        player.stdin.write(current_stdin)
        player.stdin.flush()
        
        # TODO: is it correct? Is there any other data?
        pipes = select([player.stdout, player.stderr], [], [], float_timeout)[0]

        # no data to read in player.stdout
        if player.stdout not in pipes:
            result_log['verdicts'][state.get_current_player()] = 'TL'
            state.ban_current_player()
            continue

        try:
            # TODO: what kind of const is that???
            current_stdout = os.read(player.stdout.fileno(), 1000).decode()
        except UnicodeDecodeError:
            state.ban_current_player()
            result_log['verdicts'][state.get_current_player()] = 'RE'
            continue

        if player.stderr in pipes:
            try:
                current_stderr = os.read(player.stderr.fileno(), 1000).decode()
            except UnicodeDecodeError:
                current_stderr = '[ Warning: UnicodeDecodeError exception was thrown while decoding your stderr. Please, check your output. ]'
        else:
            current_stderr = ''

        streams_log[state.get_current_player()]['stdin'].append(current_stdin)
        streams_log[state.get_current_player()]['stdout'].append(current_stdout)
        streams_log[state.get_current_player()]['stderr'].append(current_stderr)
        for stream in ('stdin', 'stdout', 'stderr'):
            for player_id in range(len(players)):
                if player_id != state.get_current_player():
                    streams_log[player_id][stream].append("[ Waiting for my turn... ]")

        try:
            state.change_state(current_stdout)
        except PresentationError:
            game_log.append(deepcopy(state.get_log()))
            state.ban_current_player('PE')
            continue
        except MoveError:
            game_log.append(deepcopy(state.get_log()))
            state.ban_current_player()
            result_log['verdicts'][state.get_current_player()] = 'PE'
            continue

        game_log.append(deepcopy(state.get_log()))
        state.change_player()

    game_log.append(deepcopy(state.get_log()))
    winner = state.get_winner()

    if players is not None:
        for player in players:
            player.kill()
            message = f'Process killed.'
            for stream in ('stdin', 'stdout', 'stderr'):
                streams_log[state.get_current_player()][stream].append(message)

    streams_log_file.write(json.dumps(streams_log))
    game_log_file.write(json.dumps(game_log))
    result_log_file.write(json.dumps(result_log))


if __name__ == '__main__':
    args = parse_args()

    streams_log_file = open(args.streams_log_file, 'w')
    checker_log_file = open(args.checker_log_file, 'w')
    game_log_file  = open(args.game_log_file,  'w')
    result_log_file  = open(args.result_log_file,  'w')

    logger.add(checker_log_file)
    
    run_test(args, streams_log_file, game_log_file, result_log_file)

    streams_log_file.close()
    checker_log_file.close()
    result_log_file.close()
    