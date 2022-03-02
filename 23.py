from IntCode.IntCode import Comp
from copy import copy

def read_input():
    return list(map(int, [line.strip() for line in open('23.in')][0].split(',')))


def part1():
    prog = read_input()
    comps = [Comp(copy(prog), input_buffer=[i], mute=True) for i in range(50)]
    while True:
        for i, comp in enumerate(comps):
            status = comp.execute()
            if status == 1:
                comp.input_buffer = [-1]
            while len(comp.out_buffer) >= 3:
                addr, x, y = comp.out_buffer[:3]
                #print(f"{i} \t -> \t {addr}")
                if addr == 255:
                    return y
                comp.out_buffer[:3] = []
                if addr < len(comps):
                    comps[addr].input_buffer += [x, y]

def part2():
    prog = read_input()
    comps = [Comp(copy(prog), input_buffer=[i], mute=True) for i in range(50)]
    NAT = None
    Y_sent = None
    idle_count = 0
    while True:
        idle = True
        for i, comp in enumerate(comps):
            status = comp.execute()
            if status == 1:
                comp.input_buffer = [-1]

            while len(comp.out_buffer) >= 3:
                idle = False
                addr, x, y = comp.out_buffer[:3]
                #print(f"{i} \t -> \t {addr}:{x},{y}")
                if addr == 255:
                    NAT = x, y
                comp.out_buffer[:3] = []
                if addr < len(comps):
                    comps[addr].input_buffer += [x, y]
        if idle:
            idle_count += 1
            if idle_count > 1:
                idle_count = 0
                comps[0].input_buffer += [NAT[0], NAT[1]]
                if Y_sent == NAT[1]:
                    return Y_sent
                Y_sent = NAT[1]

def main():
    return part1(), part2()


if __name__ == '__main__':
    print(main())