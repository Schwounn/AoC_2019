import re
import math

def read_input():
    raw = [line.strip() for line in open('12.in')]
    ret = []
    pattern = r'<x=(-?\d*), y=(-?\d*), z=(-?\d*)>'
    for line in raw:
        m = re.search(pattern, line)
        ret.append(list(map(int, m.groups())))
    return ret

def get_next_step(positions, velocities):
    next_vel = []
    for prim in range(len(positions)):
        new_vel = [v for v in velocities[prim]]
        for sec in range(len(positions)):
            if prim == sec:
                continue
            for dim in range(3):
                if positions[sec][dim] < positions[prim][dim]:
                    new_vel[dim] -= 1
                elif positions[sec][dim] > positions[prim][dim]:
                    new_vel[dim] += 1
        next_vel.append(new_vel)
    next_pos = []
    for i, pos in enumerate(positions):
        vel = next_vel[i]
        next_pos.append([p + v for p, v in zip(pos, vel)])
    return next_pos, next_vel


def get_energy(positions, velocities):
    potential = [sum(map(abs, pos)) for pos in positions]
    kinetic = [sum(map(abs, vel)) for vel in velocities]
    return sum([p * k for p, k in zip(potential, kinetic)])

def part1(positions):
    velocities = [[0, 0, 0] for pos in positions]
    for i in range(1000):
        positions, velocities = get_next_step(positions, velocities)
    return get_energy(positions, velocities)

def to_tup(vec):
    return tuple(map(tuple, vec))

def next_dim(pos, vel):
    next_vel = [v for v in vel]
    for i, p in enumerate(pos):
        for i2, p2 in enumerate(pos):
            if p == p2:
                continue
            elif p > p2:
                next_vel[i] -= 1
            else:
                next_vel[i] += 1

    next_pos = [p + v for p, v in zip(pos, next_vel)]
    return next_pos, next_vel

def sim_dim_to_end(pos, vel):
    start_pos = tuple(pos)
    start_vel = tuple(vel)
    i = 0
    while True:
        pos, vel = next_dim(pos, vel)
        i += 1
        if (tuple(pos), tuple(vel)) == (start_pos, start_vel):
            break
    return i

def part2(positions):
    positions = [[p[i] for p in positions] for i in range(3)]
    velocities = [[0, 0, 0, 0] for pos in positions]
    cycles = [sim_dim_to_end(p, v) for p, v in zip(positions, velocities)]
    return math.lcm(*cycles)


def main():
    data = read_input()
    return part1(data), part2(data)


if __name__ == '__main__':
    print(main())