from IntCode.IntCode import Comp
import copy

def read_input():
    raw = open('05.in').read().split(',')
    return list(map(int, raw))


def part1(data):
    comp = Comp(data)
    comp.execute()
    return comp.out_buffer[-1]

def part2(data):
    pass



def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))


if __name__ == '__main__':
    print(main())