import math
def read_input():
    ret = set()
    raw = [line.strip() for line in open('10.in')]
    for y, line in enumerate(raw):
        for x, c in enumerate(line):
            if c == '#':
                ret.add((x, y))
    return ret

def part1(data):
    best = 0
    for x, y in data:
        slopes = set()
        for xi, yi in data:
            if (xi, yi) == (x, y):
                continue
            dx = xi - x
            dy = yi - y
            g = math.gcd(dx, dy)
            if g == 0:
                g = max(abs(dx), abs(dy))
            dx //= g
            dy //= g
            slopes.add((dx, dy))
        best = max(best, len(slopes))
    return best


def main():
    data = read_input()
    return part1(data)


if __name__ == '__main__':
    print(main())