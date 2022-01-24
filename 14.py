import queue
import math


def get_amount_key(s):
    amount, key = s.strip().split()
    return int(amount), key


def read_input():
    ret = {}
    raw = [line.strip() for line in open('14.in')]
    for line in raw:
        l, h = line.strip().split('=>')
        amount, key = get_amount_key(h)
        recipe = [get_amount_key(s) for s in l.split(',')]
        ret[key] = (amount, recipe)
    return ret


def get_children(reactions, material):
    return [r[1] for r in reactions[material][1]]


def get_sub_components(reactions, material):
    visited = set()
    q = queue.Queue()
    q.put(material)
    while not q.empty():
        node = q.get()
        if node in visited:
            continue
        visited.add(node)
        if node in reactions:
            for amount, child in reactions[node][1]:
                q.put(child)
    visited.remove(material)
    return visited


def get_sub_components_amount(reactions, material, amount):
    required = {material : amount}
    while not (len(required) == 1 and 'ORE' in required):
        for key in required:
            if key == 'ORE':
                continue
            if key not in set().union(*[get_sub_components(reactions, k) for k in required]):
                chosen_key = key
                break
        amount = reactions[chosen_key][0]
        amount = math.ceil(required[chosen_key] / amount)
        for a, mat in reactions[chosen_key][1]:
            required[mat] = required.get(mat, 0) + a * amount
        del required[chosen_key]
    return required['ORE']

def part1(data):
    return get_sub_components_amount(data, 'FUEL', 1)


def part2(data):
    goal = 10**12
    top = goal
    bot = 1
    while top - bot != 1:
        middle = (bot + top) // 2
        if get_sub_components_amount(data, 'FUEL', middle) > goal:
            top = middle
        else:
            bot = middle
    return bot


def main():
    data = read_input()
    return part1(data), part2(data)


if __name__ == '__main__':
    print(main())