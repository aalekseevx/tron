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

def generate_level_1():
    global x, e, r, b, c, u, d
    w, h = 25, 25
    ans = [[e for _ in range(h)] for _ in range(w)]
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 1,
        'field': ans,
    }

    
def generate_level_2():
    global x, e, r, b, c, u, d
    w, h = 20, 20
    ans = [[e for _ in range(h)] for _ in range(w)]
    basic_comp = [
        [
            [x, x],
            [x, e]
        ],
        [
            [x for _ in range(8)]
        ]
    ]
    blocks = []
    for comp in basic_comp:
        blocks.append(comp)
        for _ in range(3):
            blocks.append(list(zip(*blocks[-1][::-1])))
    positions = [
        [2, 2],
        [2, 16],
        [16, 16],
        [16, 2],

        [4, 6],
        [6, 15],
        [15, 6],
        [6, 4]
    ]

    for i, pos in enumerate(positions):
        for xs, row in enumerate(blocks[i]):
            for ys, val in enumerate(row):
                ans[xs + pos[0]][ys + pos[1]] = val
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 2,
        'field': ans,
    }

def generate_level_3():
    global x, e, r, b, c, u, d
    quoter = [
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, x, e, x, x, e],
        [e, e, e, e, e, e, e, e, e, e, e, c, c, c, c],
        [e, e, e, e, e, e, e, e, e, e, x, c, c, c, c],
        [e, e, e, e, e, e, e, e, e, e, x, c, c, c, c],
        [e, e, e, e, e, e, e, e, e, e, e, c, c, c, c],
    ]
    half = [row + row[-2::-1] for row in quoter]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 3,
        'field': ans,
    }

def generate_level_4():
    global x, e, r, b, c, u, d
    quoter = [
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, d, x, x, x, e, x, x, x, d, e, e, e],
        [e, e, e, e, e, e, x, e, x, e, e, e, e, e, e],
        [e, e, e, e, e, u, x, e, x, u, e, e, e, e, e],
        [e, e, x, x, x, x, x, e, x, x, x, x, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, d, e, e, e, e, e, e, e],
        [e, e, x, x, x, x, e, e, x, x, x, x, e, e, e],
        [e, e, x, e, u, x, e, e, x, u, e, x, e, e, e],
        [e, e, x, e, u, x, e, e, x, e, e, e, e, e, e],
        [e, e, x, e, u, x, e, e, x, x, e, e, e, d, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, d, e, e],
        [e, e, e, e, e, e, e, e, e, e, d, e, e, e, u],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, u, u],
    ]
    half = [row + row[-2::-1] for row in quoter]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 4,
        'field': ans,
    }

def generate_level_5():
    global x, e, r, b, c, u, d
    quoter = [
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, e, x, e, e, e, e, e, e, e, e, e, e],
        [e, e, e, x, x, e, e, c, x, c, e, e, e, e, e],
        [e, e, x, x, x, e, e, x, x, x, e, e, e, e, e],
        [e, x, x, x, x, e, e, c, x, c, e, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, d, e],
        [e, e, e, e, e, e, d, e, e, e, e, e, e, e, e],
        [e, e, c, x, c, e, e, e, c, x, c, e, e, e, e],
        [e, e, x, x, x, e, e, c, u, x, u, c, e, e, e],
        [e, e, c, x, c, e, e, x, x, x, x, x, e, e, e],
        [e, e, e, e, e, e, e, c, u, x, u, c, e, e, e],
        [e, e, e, e, e, d, e, e, c, u, c, e, e, e, e],
        [e, e, e, e, e, e, e, e, e, e, e, e, e, e, e],
    ]
    half = [row + row[-2::-1] for row in quoter]
    ans = copy.deepcopy(half) + copy.deepcopy(half)[-2::-1]
    ans[0][0] = r
    ans[-1][-1] = b
    return {
        'level': 5,
        'field': ans,
    }

if __name__ == '__main__':
    args = parse_arguments()
    level = None
    if args.test_id == 1:
        level = generate_level_1()
    elif args.test_id == 2:
        level = generate_level_2()
    elif args.test_id == 3:
        level = generate_level_3()
    elif args.test_id == 4:
        level = generate_level_4()
    elif args.test_id == 5:
        level = generate_level_5()
    write_test(level, args.test_file)
    write_test_description(level, args.test_description_file)

