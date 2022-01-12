from IntCode.IntCode import Comp
import copy

def read_input():
    raw = open('09.in').read().split(',')
    return list(map(int, raw))


def part1(data):
    comp = Comp(data, input_buffer=[1])
    comp.execute()
    return comp.out_buffer[0]

def part2(data):
    comp = Comp(data, input_buffer=[2])
    comp.execute()
    return comp.out_buffer[0]



def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))


if __name__ == '__main__':
    print(main())