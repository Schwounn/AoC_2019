from IntCode.IntCode import Comp
import copy
import itertools

def read_input():
    raw = open('07.in').read().split(',')
    return list(map(int, raw))


def part1(data):
    seq = [0,1,2,3,4]
    best = 0
    for perm in itertools.permutations(seq):
        _input = 0
        for i in range(5):
            comp = Comp(copy.copy(data), input_buffer=[perm[i], _input])
            comp.execute()
            _input = comp.out_buffer[-1]
        best = max(best, _input)
    return best

def part2(data):
    seq = list(range(5,10))
    best = 0
    for perm in itertools.permutations(seq):
        _input = 0
        comp_list = [Comp(copy.copy(data), input_buffer=[perm[i]]) for i in range(5)]
        comp_list[0].input_buffer.append(_input)
        done = False
        while not done:
            for i in range(5):
                comp = comp_list[i]
                try:
                    comp.execute()
                except BufferError as e:
                    _input = comp.out_buffer[-1]
                    comp_list[(i + 1) % 5].input_buffer.append(_input)
                    continue
                else:
                    _input = comp.out_buffer[-1]
                    comp_list[(i + 1) % 5].input_buffer.append(_input)
                    done = True
        best = max(best, _input)
    return best



def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))


if __name__ == '__main__':
    print(main())