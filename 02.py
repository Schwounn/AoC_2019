from IntCode.IntCode import Comp
import copy

def read_input():
    raw = open('02.in').read().split(',')
    return list(map(int, raw))


def part1(data):
    data[1] = 12
    data[2] = 2
    comp = Comp(data)
    return comp.execute()[0]

def part2(data):
    for noun in range(100):
        for verb in range(100):
            data_c = copy.copy(data)
            data_c[1] = noun
            data_c[2] = verb
            comp = Comp(data_c)
            if comp.execute()[0] == 19690720:
                return 100*noun + verb



def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))


if __name__ == '__main__':
    print(main())