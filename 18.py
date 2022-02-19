from queue import PriorityQueue


def read_input():
    return [line.strip() for line in open('18.in')]


def get_start(data):
    for y, line in enumerate(data):
        if '@' in line:
            return line.index('@'), y

def get_neighbors(x, y):
    diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for (dx, dy) in diffs]


def get_all_keys(data):
    return ''.join(sorted([c for c in ''.join(data) if c.islower()]))

def part1(data):
    start = 0, get_start(data), ''
    all_keys = get_all_keys(data)
    q = PriorityQueue()
    q.put(start)
    visited = set()
    while not q.empty():
        cost, coord, keys = q.get()
        if (coord, keys) in visited:
            continue
        if keys == all_keys:
            return cost
        print(cost)
        visited.add((coord, keys))
        for nx, ny in get_neighbors(*coord):
            tile = data[ny][nx]
            if tile == '#':
                continue
            if tile.isupper() and tile.lower() not in keys:
                continue
            q.put((cost + 1, (nx, ny), ''.join(sorted(set(keys + (tile if tile.islower() else ''))))))


    return -1


def main():
    data = read_input()
    return part1(data)


if __name__ == '__main__':
    print(main())