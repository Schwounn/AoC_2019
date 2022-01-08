
def read_input():
    raw = [line.strip().split(')') for line in open('06.in')]
    parent = {}
    children = {}
    for p, c in raw:
        parent[c] = p
        if p in children:
            children[p].append(c)
        else:
            children[p] = [c]
    return parent, children


def part1(parent, children):

    def dfs(n, l):
        if n not in children:
            return l
        else:
            ret = l
            for c in children[n]:
                ret += dfs(c, l + 1)
            return ret
    return dfs('COM', 0)


def part2(parent, children):

    def is_child_of(c, p):
        length = 0
        while c != 'COM':
            if c == p:
                return True, length
            else:
                c = parent[c]
                length += 1
        return False, -1

    length = 0
    pos = parent['YOU']
    target = parent['SAN']
    while True:
        check, l = is_child_of(target, pos)
        if check:
            return l + length
        else:
            length += 1
            pos = parent[pos]



def main():
    parent, children = read_input()
    return part1(parent, children), part2(parent, children)

if __name__ == '__main__':
    print(main())