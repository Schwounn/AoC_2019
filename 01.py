import sys

#sys.setrecursionlimit(1000)
def read_input():
    ret = [int(line.strip()) for line in open('01.in')]
    return ret


def f(i):
    return i//3 - 2


def f2(i):
    if f(i) <= 0:
        return 0
    else:
        return f(i) + f2(f(i))

def part1(data):
    return sum(map(f, data))


def part2(data):
    return sum(map(f2, data))


def main():
    data = read_input()
    return part1(data), part2(data)

if __name__ == '__main__':
    print(main())