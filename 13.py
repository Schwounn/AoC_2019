import copy
from IntCode.IntCode import Comp
import time

def read_input():
    raw = open('13.in').read().split(',')
    return list(map(int, raw))


def get_screen(comp_out):
    ret = {(comp_out[i], comp_out[i + 1]) : comp_out[i + 2] for i in range(0, len(comp_out), 3)}
    return ret


def pp(screen):
    chars = ' #o-O'
    xsize, ysize = max(screen.keys())
    for y in range(ysize + 1):
        for x in range(xsize + 1):
            print(chars[screen[(x, y)]], end='')
        print()

def cmp(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

def part1(data):
    comp = Comp(data)
    status = comp.execute()
    return list(get_screen(comp.out_buffer).values()).count(2)




def part2(data):
    data[0] = 2
    comp = Comp(data, input_buffer=[], mute=True)
    prev_ball = -1, -1
    ball_dir = (1, 1)
    while True:
        status = comp.execute()
        screen = get_screen(comp.out_buffer)
        ball = [(x, y) for (x, y) in screen if screen[(x, y)] == 4][0]
        paddle = [(x, y) for (x, y) in screen if screen[(x, y)] == 3][0]

        move = cmp(ball, prev_ball) - cmp(paddle, ball)
        if status == 0:
            return screen[(-1, 0)]
        comp.input_buffer.append(move)
        prev_ball = ball

def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))

if __name__ == '__main__':
    print(main())