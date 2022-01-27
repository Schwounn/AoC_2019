
def read_input():
    return list(map(int, open('16.in').readline()))


def repeating_pattern(n, pattern):
    skipped = False
    while True:
        for r in pattern:
            for i in range(n):
                if skipped:
                    yield r
                else:
                    skipped = True


def shorten(i):
    return abs(i) % 10


def prefix_sum(data):
    s = 0
    ret = [0]
    for i in range(len(data)):
        s += data[i]
        ret.append(s)
    return ret


def FFT(data, pattern):
    ret = []
    for i in range(len(data)):
        value = sum([a * b for (a, b) in zip(data, repeating_pattern(i + 1, pattern))])
        ret.append(shorten(value))
    return ret


def FFFT(data, offset):
    s = prefix_sum(data)
    ret = [0] * offset
    for i in range(offset, len(data)):
        positive_ranges = [(j, i + j if i + j < len(data) else len(data)) for j in
                           range(i, len(data), (i + 1) * 4)]
        negative_ranges = [(j, i + j if i + j < len(data) else len(data)) for j in
                           range((i + 1) * 3 - 1, len(data), (i + 1) * 4)]
        value = sum([s[ind[1]] - s[ind[0]] for ind in positive_ranges]) - sum([s[ind[1]] - s[ind[0]] for ind in negative_ranges])
        ret.append(shorten(value))
    return ret

def part1(data):
    pattern = [0, 1, 0, -1]
    for i in range(100):
        data = FFT(data, pattern)
    return int(''.join(map(str, data[:8])))



def part2(data):
    pos = int(''.join(map(str, data[:7])))
    data = data * 10_000
    pattern = [0, 1, 0, -1]
    for i in range(100):
        print(i)
        data = FFFT(data,pos)
    return int(''.join(map(str, data[pos:pos + 8])))


def main():
    data = read_input()
    return part1(data), part2(data)

if __name__ == '__main__':
    print(main())