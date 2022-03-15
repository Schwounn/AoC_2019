
deck_len = 10007

def read_input():
    ret = [line.strip().split() for line in open('22.in')]
    for i, line in enumerate(ret):
        if line[0] == 'cut':
            ret[i] = ['cut', int(line[-1])]
        elif line[2] == 'increment':
            ret[i] = ['inc', int(line[-1])]
        else:
            ret[i] = ['new']
    return ret


def part1():
    instructions = read_input()
    deck = list(range(deck_len))
    for ins in instructions:
        if len(ins) == 1:
            deck = deck[::-1]
        elif ins[0] == 'cut':
            deck = deck[ins[1]:] + deck[:ins[1]]
        else:
            new_deck = [0] * deck_len
            for i, val in enumerate(deck):
                new_deck[(i * ins[1]) % len(deck)] = val
            deck = new_deck
    return deck.index(2019)


def main():
    return part1()


if __name__ == '__main__':
    print(main())