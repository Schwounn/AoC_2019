from IntCode.IntCode import Comp
from copy import copy

def read_input():
    raw = open('19.in').read().split(',')
    return list(map(int, raw))


def part1(data):
    count = 0
    for x in range(50):
        for y in range(50):
            comp = Comp(copy(data), input_buffer=[x, y], mute=True)
            comp.execute()
            count += comp.out_buffer[-1]
    return count


def part2(data):
    x, y = 0, 99
    while True:
        comp = Comp(copy(data), input_buffer=[x, y], mute=True)
        comp.execute()
        res = comp.out_buffer[-1]
        if res:
            comp = Comp(copy(data), input_buffer=[x + 99, y - 99], mute=True)
            comp.execute()
            res2 = comp.out_buffer[-1]
            if res2:
                return x * 10_000 + y - 99
            y += 1
        else:
            x += 1

def main():
    data = read_input()
    return part1(copy(data)), part2(copy(data))

if __name__ == '__main__':
    print(main())