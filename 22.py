

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


def gcd_ext(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_ext(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y


def part1():
    instructions = read_input()
    deck_len = 10007
    position = 2019
    for ins in instructions:
        if len(ins) == 1:
            position = - position - 1
        elif ins[0] == 'cut':
            position -= ins[1]
        else:
            position = (position * ins[1]) % deck_len
    return position % deck_len


def part2():
    instructions = read_input()
    deck_len = 119315717514047
    shuffle_reps = 101741582076661

    k, m = 1, 0 # kx + m
    for ins in instructions:
        if len(ins) == 1:
            m = - m - 1
            k = -k
        elif ins[0] == 'cut':
            m -= ins[1]
        else:
            k = (k * ins[1])
            m = (m * ins[1])
        k %= deck_len
        m %= deck_len
    position = 2020
    inv = gcd_ext(k - 1, deck_len)[1]
    kn = pow(k, shuffle_reps, deck_len)
    mn = (m * (kn - 1) * inv) % deck_len
    kn_inv = gcd_ext(kn, deck_len)[1]
    return ((position - mn) * kn_inv) % deck_len



def main():
    return part1(), part2()


if __name__ == '__main__':
    print(main())