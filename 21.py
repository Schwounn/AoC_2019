from IntCode.IntCode import Comp


def read_input():
    return list(map(int, [line.strip() for line in open('21.in')][0].split(',')))


def part1():
    prog = read_input()
    comp = Comp(prog, input_buffer=[], mute=True)

    ins = [
        "NOT C J",
        "AND D J",
        "NOT B T",
        "AND D T",
        "OR T J",
        "NOT A T",
        "OR T J"

    ]

    for i in ins:
        comp.feed_ascii(i + '\n')
    comp.feed_ascii("WALK\n")
    comp.execute()
    return comp.out_buffer[-1]


def part2():
    prog = read_input()
    comp = Comp(prog, input_buffer=[], mute=True)

    ins = [
        "NOT C J",
        "AND D J",
        "AND H J",
        "NOT B T",
        "AND D T",
        "OR T J",
        "NOT A T",
        "OR T J"

    ]

    for i in ins:
        comp.feed_ascii(i + '\n')
    comp.feed_ascii("RUN\n")
    comp.execute()
    return comp.out_buffer[-1]


def main():
    return part1(), part2()


if __name__ == '__main__':
    print(main())