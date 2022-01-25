from IntCode.IntCode import Comp
import copy
import queue

moves = {
    (0, 1): 1,
    (0, -1): 2,
    (-1, 0): 3,
    (1, 0): 4
}

def read_input():
    raw = open('15.in').read().split(',')
    return list(map(int, raw))

def grid_size(s):
    minx, maxx = min([p[0] for p in s]), max([p[0] for p in s])
    miny, maxy = min([p[1] for p in s]), max([p[1] for p in s])
    return minx, miny, maxx, maxy

def pp(s):
    x0, y0, x1, y1 = grid_size(s)
    trans = '#.G'
    for y in range(y1, y0 - 1, -1):
        for x in range(x1, x0 - 1, -1):
            print(trans[s[(x, y)]] if (x, y) in s else ' ', end='')
        print()


def get_neighbors(pos):
    return [(pos[0] + x, pos[1] + y) for (x, y) in moves]

def get_path(pos, parents):
    path_nodes = [pos]
    while parents[pos]:
        pos = parents[pos]
        path_nodes.append(pos)
    path_nodes = path_nodes[::-1]
    ret = []
    for i in range(len(path_nodes) - 1):
        mov = tuple([b - a for a, b in zip(path_nodes[i], path_nodes[i + 1])])
        ret.append(moves[mov])
    return ret


def get_closest_missing(pos, known_map):
    return get_closest_path(pos, None, known_map)


def get_closest_path(pos, goal, known_map):
    q = queue.Queue()
    visited = set()
    parents = {}
    q.put((pos, None))
    while not q.empty():
        node, parent = q.get()
        if node in visited:
            continue
        visited.add(node)
        parents[node] = parent
        if goal is None:
            if node not in known_map:
                return node, get_path(node, parents), parent
        elif node == goal:
            return node, get_path(node, parents), parent

        if known_map[node] != 0:
            for n in get_neighbors(node):
                if n in known_map and known_map[n] == 0:
                    continue
                q.put((n, node))
    return None, None, None

def get_map(prog):

    comp = Comp(prog, input_buffer=[], mute=True)

    known_map = {(0, 0): 1}
    robot_pos = (0, 0)
    closest, path, parent = get_closest_missing(robot_pos, known_map)
    while closest:
        comp.input_buffer += path
        comp.execute()
        response = comp.out_buffer.pop()
        if response == 0:
            robot_pos = parent
        else:
            robot_pos = closest
        known_map[closest] = response
        closest, path, parent = get_closest_missing(robot_pos, known_map)
    #pp(known_map)
    return known_map


def part1(prog):
    known_map = get_map(prog)
    goal = [node for node in known_map if known_map[node] == 2][0]
    node, path, parent = get_closest_path((0, 0), goal, known_map)
    return len(path)


def part2(prog):
    known_map = get_map(prog)
    goal = [node for node in known_map if known_map[node] == 2][0]
    ret = 0
    nodes = [node for node in known_map if known_map[node] == 1]
    for node in nodes:
        n, path, parent = get_closest_path(node, goal, known_map)
        ret = max(ret, len(path))
    return ret


def main():
    data = read_input()
    return part1(copy.copy(data)), part2(copy.copy(data))


if __name__ == '__main__':
    print(main())