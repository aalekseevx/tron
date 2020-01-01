import json
import copy
from generator_tools import *

# Block
x = 'X'
# Empty
e = '.'
# Red player
r = 'R'
# Blue player
b = 'B'
# Coin
c = 'C'
# SpeedUp
u = 'U'
# SpeedDown
d = 'D'

def generate_level_6():
    global x, e, r, b, c, u, d
    quoter = [
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, d, e, e, e, x, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, x, c, e, e, x, c, e, e, e, x, e, e, e, e],
        [e, e, e, x, c, e, e, e, e, x, c, e, e, e, e, e, e, e],
        [e, e, x, c, e, e, e, e, e, e, x, c, e, e, e, e, e, e],
        [e, x, c, e, e, e, e, e, e, e, e, x, c, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, x, c, e, e, e, e],
        [e, e, e, e, e, c, x, c, e, e, e, e, e, x, e, e, e, e],
        [e, e, e, e, e, x, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, c, x, u, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, x, x, e, e, e, e, e, e, x, x, e, e, e, e, e, d, e],
        [e, e, e, x, x, x, e, x, x, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, d, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
    ]
    half = [row + row[-2::-1] for row in quoter]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 6,
        'field': ans,
    }

def generate_level_7():
    global x, e, r, b, c, u, d
    half = [
        [r, e, c, c, x, c, c, c, e, x, c, e, e, c, x, e, c, c, c],
        [e, e, x, x, x, x, x, x, e, x, x, e, x, c, x, e, x, x, x],
        [e, e, x, e, e, x, c, x, e, e, x, e, x, c, x, e, e, e, c],
        [e, e, e, e, e, x, e, e, e, e, x, e, x, c, c, e, x, e, x],
        [x, x, x, e, e, x, e, e, e, x, x, e, x, x, x, e, x, e, c],
        [x, c, c, e, x, x, x, x, e, x, u, e, e, e, e, e, x, e, x],
        [x, x, x, e, e, e, e, e, e, x, e, e, e, e, e, e, x, e, e],
        [e, e, e, e, x, x, x, x, e, x, x, e, x, x, e, e, x, x, e],
        [e, x, x, e, c, x, x, e, e, e, e, e, d, x, e, e, e, e, e],
        [e, c, x, e, x, x, x, e, x, x, x, x, e, x, e, x, x, x, x]
    ]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[-1][0] = b
    return {
        'level': 7,
        'field': ans,
    }

def generate_level_8():
    global x, e, r, b, c, u, d
    half = [([e] * 37)] * 11 + [[x] * 37] + [
        [e, c, e, e, e, e, e, e, e, e, x, e, e, e, d, e, e, e, e, e, e, e, e, e, e, e, x, c, e, e, e, e, e, e, e, e, e],
        [e, x, e, e, e, e, e, e, e, e, x, e, x, e, e, e, e, e, e, x, e, e, e, x, e, e, e, e, x, x, x, x, x, x, e, e, e],
        [e, c, e, x, x, x, e, e, e, e, x, e, x, x, e, e, e, e, x, x, x, e, e, e, x, e, e, e, x, c, c, c, c, c, e, e, e],
        [e, x, e, u, x, c, e, e, e, e, x, e, x, x, x, e, e, e, x, c, x, e, e, e, x, e, x, u, x, c, c, c, c, c, e, e, e],
        [e, c, e, x, x, x, e, e, e, e, x, e, x, x, x, x, e, e, e, e, e, e, e, x, e, e, e, e, x, x, x, x, x, x, e, e, e],
        [e, x, e, e, e, e, e, e, e, e, u, e, x, x, x, c, e, e, e, e, e, e, e, x, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, x, x, c, e, e, e, x, x, x, e, d, e, e, e, x, e, e, e, e, e, e, e, e, e, e]
    ]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[12][0] = r
    ans[-13][0] = b
    return {
        'level': 8,
        'field': ans,
    }

def generate_level_9():
    global x, e, r, b, c, u, d
    half = [
        [r, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, e, e, c, e, c, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, e, e, e, c, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, e, e, c, e, c, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, c, c, x, e, e, e, x, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, c, c, x, e, e, e, x, e, e, x, x, x, x, x],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, c, c, x, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, c, c, x, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, x, x, x, x, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, x, x, x, x, x, x, e, e, e, d, x, x, x, x, x, x, x, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, x, c, c, c, c, x, e, e, e, e, x, c, c, c, c, c, x, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, x, c, u, u, c, x, e, e, e, u, x, c, c, d, c, c, x, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, x, x, c, c, c, c, x, x, x, x, x, x, c, c, c, c, c, x, x, x, x, x, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, c, c, c, c, x, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, c, d, c, c, x, e],
    ]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[-1][0] = b
    return {
        'level': 9,
        'field': ans,
    }

def generate_level_10():
    global x, e, r, b, c, u, d
    half = [
        [r, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, c, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, c, x, c, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, c, x, x, x, c, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, c, x, c, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, c, x, c, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, c, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, c, c, c, c, c, c, c],
        [e, e, e, e, e, e, e, e, e, e, e, c, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, e, e, e, e, c, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, e, e, e, c, x, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, e, e, e, c, x, x, e, e, x, x, x, x, x],
        [e, e, e, e, e, e, e, e, c, x, x, e, e, c, e, x, x, x, x],
        [e, e, e, e, e, e, e, e, c, x, x, e, e, e, e, x, x, c, c],
        [e, e, e, e, e, e, e, c, x, x, x, x, e, e, x, x, x, x, c],
        [e, e, e, e, e, e, e, c, x, x, x, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, e, c, x, x, x, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, e, c, x, x, x, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, c, x, x, x, x, x, x, x, x, x, x, x, x],
        [e, e, e, e, e, e, c, x, x, x, x, x, x, x, e, e, e, e, e],
        [e, e, e, e, e, e, c, x, x, x, x, x, e, e, e, e, e, e, e],
        [e, e, e, e, e, c, x, x, x, x, x, e, e, x, e, e, e, e, x],
        [e, e, e, e, e, c, x, x, x, x, e, e, x, e, x, e, e, x, e],
        [e, e, e, e, e, c, x, x, x, x, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, c, x, x, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, c, x, x, x, x, e, e, x, e, e, e, x, x, e, e],
        [e, e, e, e, c, x, c, x, x, e, x, e, x, e, x, e, e, x, e],
        [e, e, e, e, c, x, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, c, x, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, c, x, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, c, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, c, x, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, c, x, x, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, c, x, x, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, c, x, x, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, c, c, c, c, c, c, c, c, c],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
    ]
    ans = [row + row[::-1] for row in half]
    ans[0][-1] = b
    return {
        'level': 10,
        'field': ans,
    }

if __name__ == '__main__':
    args = parse_arguments()
    level = None
    if args.test_id == 6:
        level = generate_level_6()
    elif args.test_id == 7:
        level = generate_level_7()
    elif args.test_id == 8:
        level = generate_level_8()
    elif args.test_id == 9:
        level = generate_level_9()
    elif args.test_id == 10:
        level = generate_level_10()
    write_test(level, args.test_file)
    write_test_description(level, args.test_description_file)

