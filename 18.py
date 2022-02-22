from queue import PriorityQueue


def read_input():
    return [line.strip() for line in open('18.in')]


def get_start(data, key='@'):
    for y, line in enumerate(data):
        if key in line:
            return line.index(key), y
    return None, None

def get_neighbors(x, y):
    diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for (dx, dy) in diffs]


def get_all_keys(data):
    return ''.join(sorted([c for c in ''.join(data) if c.islower()]))


def get_paths_from(key, data):
    start = 0, get_start(data, key=key), ''
    all_keys = get_all_keys(data)
    q = PriorityQueue()
    q.put(start)
    visited = set()
    paths = {}
    while not q.empty():
        cost, coord, doors = q.get()
        if coord in visited:
            continue
        visited.add(coord)
        if data[coord[1]][coord[0]].islower():
            paths[data[coord[1]][coord[0]]] = (cost, doors)
        if len(paths) == len(all_keys):
            return paths
        for nx, ny in get_neighbors(*coord):
            ndoors = doors
            tile = data[ny][nx]
            if tile == '#':
                continue
            if tile.isupper():
                ndoors += tile
            q.put((cost + 1, (nx, ny), ndoors))
    return paths


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
    return get_paths_from('@', data)


if __name__ == '__main__':
    print(main())
