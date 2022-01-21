from IntCode.IntCode import Comp
def read_input():
    raw = open('11.in').read().split(',')
    return list(map(int, raw))

def grid_size(s):
    minx, maxx = min([p[0] for p in s]), max([p[0] for p in s])
    miny, maxy = min([p[1] for p in s]), max([p[1] for p in s])
    return minx, miny, maxx, maxy


def pp(s):
    x0, y0, x1, y1 = grid_size(s)
    for y in range(y1, y0 - 1, -1):
        for x in range(x1, x0 - 1, -1):
            print('#' if (x, y) in s else ' ', end='')
        print()


def part1(data):
    white_set = set()
    paint_set = set()
    comp = Comp(data, input_buffer=[])
    x, y = 0, 0
    direction = (0, 1)
    while True:
        comp.input_buffer.append(1 if (x, y) in white_set else 0)
        status = comp.execute()
        paint, move = comp.out_buffer[-2:]
        # Paint
        if paint == 1:
            white_set.add((x, y))
        elif (x, y) in white_set:
            white_set.remove((x, y))
        paint_set.add((x, y))
        # Move
        if move == 1:
            direction = -direction[1], direction[0]
        else:
            direction = direction[1], -direction[0]
        x, y = x + direction[0], y + direction[1]
        if status == 0:
            break

    return len(paint_set)

def part2(data):
    white_set = set()
    white_set.add((0, 0))
    comp = Comp(data, input_buffer=[])
    x, y = 0, 0
    direction = (0, 1)
    while True:
        comp.input_buffer.append(1 if (x, y) in white_set else 0)
        status = comp.execute()
        paint, move = comp.out_buffer[-2:]
        # Paint
        if paint == 1:
            white_set.add((x, y))
        elif (x, y) in white_set:
            white_set.remove((x, y))
        # Move
        if move == 1:
            direction = -direction[1], direction[0]
        else:
            direction = direction[1], -direction[0]
        x, y = x + direction[0], y + direction[1]
        if status == 0:
            break
    pp(white_set)


def main():
    data = read_input()
    return part1(data), part2(data)

if __name__ == '__main__':
    print(main())