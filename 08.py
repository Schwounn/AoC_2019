
def read_input():
    raw = open('08.in').readline()
    return raw

def get_layers(data):
    lines = [data[i: i + 25] for i in range(0, len(data), 25)]
    layers = [lines[i: i + 6] for i in range(0, len(lines), 6)]
    return layers

def part1(data):
    layers = get_layers(data)
    fewest_0, best_score = float('inf'), -1
    for lay in layers:
        s = ''.join(lay)
        z_count = s.count('0')
        score = s.count('1') * s.count('2')
        fewest_0, best_score = (z_count, score) if z_count < fewest_0 else (fewest_0, best_score)

    return best_score


def part2(data):
    layers = get_layers(data)
    ret = list(map(list, layers[0]))
    for lay in layers[1:]:
        #print(lay[0][3])
        for y, line in enumerate(lay):
            for x, c in enumerate(line):
                if ret[y][x] == '2':
                    ret[y][x] = c

    translation = {
        '0' : ' ',
        '1' : '#',
        '2' : ' '
    }
    for line in ret:
        for c in line:
            print(translation[c], end='')
        print()


def main():
    data = read_input()
    return part1(data), part2(data)


if __name__ == '__main__':
    print(main())