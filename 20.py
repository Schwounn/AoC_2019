from queue import PriorityQueue

def read_input():
    return [list(line.rstrip()) for line in open('20.in')]


def get_tile(x, y, data):
    if y < len(data) and y >= 0:
        if x < len(data[y]) and x >= 0:
            return data[y][x]
    return ' '


def get_neighbors(x, y):
    diffs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x + dx, y + dy) for (dx, dy) in diffs]


def get_labels(data):
    labels = {}
    port_pairs = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == '.':
                neighbors = [(nx, ny, get_tile(nx, ny, data))
                             for nx, ny in get_neighbors(x, y)
                             if get_tile(nx, ny, data).isalpha()]
                if neighbors:
                    nx1, ny1, n = neighbors[0]
                    n = n + [get_tile(nx, ny, data)
                             for nx, ny in get_neighbors(nx1, ny1)
                             if get_tile(nx, ny, data).isalpha()][0]
                    n = ''.join(sorted(n))
                    labels[(x, y)] = n
                    if n in port_pairs:
                        port_pairs[n] += [(x, y)]
                    else:
                        port_pairs[n] = [(x, y)]
    return labels, port_pairs



def find_path(data):
    labels, port_pairs = get_labels(data)
    start, stop = port_pairs['AA'][0], port_pairs['ZZ'][0]
    q = PriorityQueue()
    visited = set()
    q.put((0, start))
    while not q.empty():
        cost, node = q.get()
        if node in visited:
            continue
        visited.add(node)
        if node == stop:
            return cost
        for nx, ny in get_neighbors(*node):
            t = get_tile(nx, ny, data)
            if t == '.':
                q.put((cost + 1, (nx, ny)))
        if node in labels and node != start and node != stop:
            port = labels[node]
            destination = [p for p in port_pairs[port] if p != node][0]
            q.put((cost + 1, destination))
    return -1


def is_inner(x, y, data):
    padding = 5
    xmax = max(map(len, data))
    ymax = len(data)
    return not (x < padding or x > (xmax - padding) or y < padding or y > (ymax - padding))


def find_path_rec(data):
    labels, port_pairs = get_labels(data)
    start, stop = port_pairs['AA'][0], port_pairs['ZZ'][0]
    q = PriorityQueue()
    visited = set()
    q.put((0, start, 0))
    while not q.empty():
        cost, node, level = q.get()
        if (node, level) in visited:
            continue
        visited.add((node, level))
        if node == stop and level == 0:
            return cost
        for nx, ny in get_neighbors(*node):
            t = get_tile(nx, ny, data)
            if t == '.':
                q.put((cost + 1, (nx, ny), level))
        if node in labels and node != start and node != stop:
            port = labels[node]
            destination = [p for p in port_pairs[port] if p != node][0]
            if is_inner(*node, data) or level > 0:
                q.put((cost + 1, destination, level + (1 if is_inner(*node, data) else -1)))
    return -1

def part1():
    data = read_input()
    return find_path(data)

def part2():
    data = read_input()
    return find_path_rec(data)


def main():
    return part1(), part2()


if __name__ == '__main__':
    print(main())