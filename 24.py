

def read_input():
    return [line.strip() for line in open('24.in')]


def is_on_grid(x, y):
    return x >= 0 and x < 5 and y >=0 and y < 5


def count_neighbors(x, y, grid):
    neighborhood = [(x, y) for y in range(-1, 2) for x in range(-1, 2) if (x or y) and (not x or not y)]
    return len([grid[y + ny][x + nx] for nx, ny in neighborhood if is_on_grid(x + nx, y + ny) and grid[y + ny][x + nx] == '#'])


def get_next(grid):
    ret = []
    for y in range(5):
        line = []
        for x in range(5):
            c = grid[y][x]
            ns = count_neighbors(x, y, grid)
            if (c == '#' and ns == 1) or (c == '.' and (ns == 1 or ns == 2)):
                line.append('#')
            else:
                line.append('.')
        ret.append(''.join(line))
    return ret

def pp(grid):
    for line in grid:
        print(line)
    print()

def biodiversity(grid):
    grid = ''.join(grid)
    ret = 0
    for i, c in enumerate(grid):
        if c == '#':
            ret += 2**i
    return ret


def part1():
    grid = read_input()
    visited = set()
    while True:
        #pp(grid)
        b = biodiversity(grid)
        if b in visited:
            return b
        visited.add(b)
        grid = get_next(grid)
    return count_neighbors(0, 0, grid)


def to_set(grid):
    ret = set()
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '#':
                ret.add((x, y, 0))
    return ret

def get_neighbors_rec(x, y, lvl):
    ret = []
    neighborhood = [(x + nx, y + ny) for ny in range(-1, 2) for nx in range(-1, 2) if (nx or ny) and (not nx or not ny)]
    for nx, ny in neighborhood:
        if (nx, ny) == (2, 2):
            if (x, y) == (1, 2):
                ret += [(0, y, lvl -1) for y in range(5)]
            elif (x, y) == (3, 2):
                ret += [(4, y, lvl -1) for y in range(5)]
            elif (x, y) == (2, 1):
                ret += [(x, 0, lvl -1) for x in range(5)]
            else:
                ret += [(x, 4, lvl -1) for x in range(5)]
        elif nx == 5:
            ret.append((3, 2, lvl + 1))
        elif nx == -1:
            ret.append((1, 2, lvl + 1))
        elif ny == 5:
            ret.append((2, 3, lvl + 1))
        elif ny == -1:
            ret.append((2, 1, lvl + 1))
        else:
            ret.append((nx, ny, lvl))
    return ret


def get_next_rec(grid):
    neighbor_counts = {}
    for alive in grid:
        neighbors = get_neighbors_rec(*alive)
        for n in neighbors:
            neighbor_counts[n] = neighbor_counts.get(n, 0) + 1
    ret = set()
    for node, count in neighbor_counts.items():
        if (node in grid and count == 1) or (node not in grid and (count == 1 or count == 2)):
            ret.add(node)
    return ret


def part2():
    grid = to_set(read_input())
    for i in range(200):
        grid = get_next_rec(grid)
    return len(grid)

def main():
    return part1(), part2()


if __name__ == '__main__':
    print(main())