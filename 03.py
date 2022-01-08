import numpy as np
def separate(s):
    return s[0], int(s[1:])

def read_input():
    ret = [list(map(separate, line.strip().split(','))) for line in open('03.in')]

    return ret


def orientation(a, b, c):
    return np.sign((b[1] - a[1]) * (c[0] - b[0]) - (c[1] - b[1]) * (b[0] - a[0]))


def is_intersect(a, b):
    return (orientation(a[0], a[1], b[0]) != orientation(a[0], a[1], b[1]) and
        orientation(b[0], b[1], a[0]) != orientation(b[0], b[1], a[1]))

def get_intersection(a, b):
    if is_intersect(a, b):
        if a[0][0] == a[1][0]:
            x = a[0][0]
        else:
            x = b[0][0]
        if a[0][1] == a[1][1]:
            y = a[0][1]
        else:
            y = b[0][1]
        return (x, y)
    else:
        return None


def generate_line_segments(path):
    x, y = 0, 0
    ret = []
    for ins in path:
        seg = [(x, y)]
        if ins[0] == 'R':
            x += ins[1]
        elif ins[0] == 'L':
            x -= ins[1]
        elif ins[0] == 'D':
            y -= ins[1]
        else:
            y += ins[1]
        seg.append((x, y))
        ret.append(seg)
    return ret


def length(a):
    return abs(a[0][0] - a[1][0]) + abs(a[0][1] - a[1][1])


def part1(data):
    first, second = list(map(generate_line_segments, data))
    intersections = []
    closest = 9999999999999
    for l1 in first:
        for l2 in second:
            intersection = get_intersection(l1, l2)
            if intersection is not None and intersection != (0, 0):
                closest = min(closest, sum(map(abs, intersection)))
                intersections.append(intersection)
    return closest


def part2(data):
    first, second = list(map(generate_line_segments, data))
    intersections = {}
    dist = 0
    for l1 in first:
        for l2 in second:
            intersection = get_intersection(l1, l2)
            if intersection is not None and intersection != (0, 0):
                intersections[intersection] = intersections.get(intersection, 0) + dist + length((l1[0], intersection))
        dist += length(l1)
    dist = 0
    for l1 in second:
        for l2 in first:
            intersection = get_intersection(l1, l2)
            if intersection is not None and intersection != (0, 0):
                intersections[intersection] = intersections.get(intersection, 0) + dist + length((l1[0], intersection))
        dist += length(l1)
    return min(intersections.values())


def main():
    data = read_input()
    return part1(data), part2(data)

if __name__ == '__main__':
    print(main())