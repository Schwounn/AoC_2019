from collections import Counter
def read_input():
    raw = open('04.in').readline().strip()
    return [int(i) for i in raw.split('-')]


def is_valid(s):
    if len(s) != 6:
        return False
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            break
    else:
        return False
    return True

def is_valid2(s):
    if not is_valid(s):
        return False
    c = Counter(s)
    return 2 in c.values()



def part1(start, stop):
    count = 0
    for i in range(start, stop + 1):
        if is_valid(str(i)):
            count += 1
    return count


def part2(start, stop):
    count = 0
    for i in range(start, stop + 1):
        if is_valid2(str(i)):
            count += 1
    return count


def main():
    start, stop = read_input()
    return part1(start, stop), part2(start, stop)

if __name__ == '__main__':
    print(main())