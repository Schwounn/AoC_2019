from queue import PriorityQueue
from copy import copy

def read_input():
    return [list(line.strip()) for line in open('18.in')]


def get_start(data, key='@'):
    for y, line in enumerate(data):
        if key in line:
            return line.index(key), y
    return None, None

def get_neighbors(x, y):
    diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for (dx, dy) in diffs]


def get_all_keys(data):
    return ''.join(sorted([c for c in ''.join([''.join(line) for line in data]) if c.islower()]))


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


def replace_start(data):
    x, y = get_start(data)
    data[y - 1][x - 1:x + 2] = ['1', '#', '2']
    data[y][x - 1:x + 2] = ['#', '#', '#']
    data[y + 1][x - 1:x + 2] = ['3', '#', '4']


def part2(data):
    replace_start(data)
    start = 0, ('1', '2', '3', '4'), ''
    all_keys = get_all_keys(data)
    q = PriorityQueue()
    q.put(start)
    visited = set()
    paths = {key: get_paths_from(key, data) for key in all_keys + '1234'}
    while not q.empty():
        cost, node, keys = q.get()
        if (node, keys) in visited:
            continue
        if all(k in keys for k in all_keys):
            return cost
        visited.add((node, keys))
        for i, k in enumerate(node):
            for nk in [i for i in paths[k] if i not in keys]:
                if not all(elem in keys for elem in paths[k][nk][1].lower()):
                    continue
                nnode = list(node)
                nnode[i] = nk
                nnode = tuple(nnode)
                q.put((cost + paths[k][nk][0], nnode, ''.join(sorted(set(keys + nk)))))
    return -1

def part1(data):
    start = 0, '@', ''
    all_keys = get_all_keys(data)
    q = PriorityQueue()
    q.put(start)
    visited = set()
    paths = {key: get_paths_from(key, data) for key in all_keys + '@'}
    while not q.empty():
        cost, k, keys = q.get()
        if (k, keys) in visited:
            continue
        if all(k in keys for k in all_keys):
            return cost
        visited.add((k, keys))
        for nk in [i for i in paths[k] if i not in keys]:
            if not all(elem in keys for elem in paths[k][nk][1].lower()):
                continue
            q.put((cost + paths[k][nk][0], nk, ''.join(sorted(set(keys + nk)))))
    return -1


def main():
    data = read_input()
    return part1(data), part2(copy(data))


if __name__ == '__main__':
    print(main())
