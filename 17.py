from IntCode.IntCode import Comp
from copy import copy

def read_input():
    raw = open('17.in').read().split(',')
    return list(map(int, raw))


def get_alignment(x, y, grid):
    neighbors = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    return x * y if all(map(lambda c : c != '.',
                            [grid[y + yd][x + xd] for xd, yd in neighbors
                             if (y + yd) >= 0 and (y + yd) < len(grid) and (x + xd) >= 0 and (x + xd) < len(grid[0])])) else 0


def part1(data):
    comp = Comp(data, mute=True)
    comp.execute()
    out = map(chr, comp.out_buffer)
    grid = []
    line = []
    for c in out:
        if c == '\n':
            if line:
                grid.append(line)
            line = []
        else:
            line.append(c)
    ret = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            ret += get_alignment(x, y, grid)

    return ret


def find_bot(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c not in '.#':
                return (x, y), c

def get_tile(coord, grid):
    if coord[0] < len(grid[0]) and coord[0] >= 0 and coord[1] < len(grid) and coord[1] >= 0:
        return grid[coord[1]][coord[0]]
    else:
        return '.'

def next_move(grid, bot):
    dir_str = '^<v>'
    dir_i = dir_str.index(bot[1])
    dir_map = {
        'v': (0, 1),
        '^': (0, -1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    l_map = {
        '<': (0, 1),
        '>': (0, -1),
        '^': (-1, 0),
        'v': (1, 0)
    }
    r_map = {
        '>': (0, 1),
        '<': (0, -1),
        'v': (-1, 0),
        '^': (1, 0)
    }
    next_coord = bot[0][0] + dir_map[bot[1]][0], bot[0][1] + dir_map[bot[1]][1]
    next_tile = get_tile(next_coord, grid)
    l_coord = bot[0][0] + l_map[bot[1]][0], bot[0][1] + l_map[bot[1]][1]
    r_coord = bot[0][0] + r_map[bot[1]][0], bot[0][1] + r_map[bot[1]][1]
    l_tile = get_tile(l_coord, grid)
    r_tile = get_tile(r_coord, grid)
    if next_tile == '#':
        return 1, (next_coord, bot[1])
    elif l_tile == '#':
        return 'L', (bot[0], dir_str[(dir_i + 1) % len(dir_str)])
    elif r_tile == '#':
        return 'R', (bot[0], dir_str[dir_i - 1])
    else:
        return None, bot

def squash_int(l):
    i = 0
    while i < len(l) - 1:
        if isinstance(l[i], int) and isinstance(l[i + 1], int):
            l[i] += l.pop(i + 1)
        else:
            i += 1

def find_path(grid):
    bot = find_bot(grid)
    path = []
    while True:
        move, bot = next_move(grid, bot)
        if move is None:
            break
        elif isinstance(move, int) and len(path) > 0 and isinstance(path[-1], int):
            path[-1] += move
        else:
            path.append(move)
    return path

def path_to_str(path):
    ret = []
    for p in path:
        p = str(p)
        for c in p:
            ret.append(ord(c))
        ret.append(ord(','))
    return ret[:-1] + [ord('\n')]


def find_solution(m, a, b, c):
    m = ''.join(map(str, m))
    a = ''.join(map(str, a))
    b = ''.join(map(str, b))
    c = ''.join(map(str, c))
    if m.replace(a, '').replace(b, '').replace(c, '') != '':
        return None
    ret = []
    while m:
        if m.startswith(a):
            ret.append('A')
            m = m.replace(a, '', 1)
        elif m.startswith(b):
            ret.append('B')
            m = m.replace(b, '', 1)
        elif m.startswith(c):
            ret.append('C')
            m = m.replace(c, '', 1)
    return ret

def compress_path(path):
    for a1 in range(len(path)):
        for a2 in range(a1, len(path)):
            a = path[a1:a2]
            if len(path_to_str(a)) > 20:
                break
            for b1 in range(a2, len(path)):
                for b2 in range(b1, len(path)):
                    b = path[b1:b2]
                    if len(path_to_str(b)) > 20:
                        break
                    for c1 in range(b2, len(path)):
                        for c2 in range(c1, len(path)):
                            c = path[c1:c2]
                            if len(path_to_str(c)) > 20:
                                break
                            sol = find_solution(path, a, b, c)
                            if sol:
                                return path_to_str(sol), path_to_str(a), path_to_str(b), path_to_str(c)

def part2(data):
    comp = Comp(copy(data), mute=True)
    comp.execute()
    out = ''.join(map(chr, comp.out_buffer))
    grid = out.strip().split('\n')
    path = find_path(grid)
    m, a, b, c = compress_path(path)
    prog = copy(data)
    prog[0] = 2
    ins = m + a + b + c + [ord('n'), ord('\n')]
    comp = Comp(prog, input_buffer=ins, mute=True)
    comp.execute()

    return comp.out_buffer[-1]


def main():
    data = read_input()
    return part1(copy(data)), part2(copy(data))

if __name__ == '__main__':
    print(main())