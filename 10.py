import math
def read_input():
    ret = set()
    raw = [line.strip() for line in open('10.in')]
    for y, line in enumerate(raw):
        for x, c in enumerate(line):
            if c == '#':
                ret.add((x, y))
    return ret

def get_slope(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    g = math.gcd(dx, dy)
    if g == 0:
        g = max(abs(dx), abs(dy))
    dx //= g
    dy //= g
    return dx, dy

def part1(data):
    best = 0
    for x, y in data:
        slopes = set()
        for xi, yi in data:
            if (xi, yi) == (x, y):
                continue
            dx, dy = get_slope(xi, yi, x, y)
            slopes.add((dx, dy))
        best = max(best, len(slopes))
    return best


def part2(data):
    best = 0
    best_coord = (-1, -1)
    for x, y in data:
        slopes = set()
        for xi, yi in data:
            if (xi, yi) == (x, y):
                continue
            dx, dy = get_slope(xi, yi, x, y)
            slopes.add((dx, dy))
        if len(slopes) > best:
            best_coord = (x, y)
        best = max(best, len(slopes))
    slp_to_ast = {}
    for xi, yi in data:
        if (xi, yi) == best_coord:
            continue
        slp = get_slope(xi, yi, best_coord[0], best_coord[1])
        angle = -(math.atan2(-slp[1], slp[0]) - (math.pi / 2))
        if angle < 0:
            angle += math.pi * 2
        dx = xi - best_coord[0]
        dy = yi - best_coord[1]
        slp_to_ast[angle] = slp_to_ast.get(angle, []) + [(dx**2 + dy**2, (xi, yi))]
    for l in slp_to_ast.values():
        l.sort()
    blast_order = []
    while slp_to_ast:
        keys = sorted(slp_to_ast.keys())
        for key in keys:
            blast_order.append(slp_to_ast[key].pop(0)[1])
            if len(slp_to_ast[key]) == 0:
                del slp_to_ast[key]

    return blast_order[199][0] * 100 + blast_order[199][1]


def main():
    data = read_input()
    return part1(data), part2(data)


if __name__ == '__main__':
    print(main())