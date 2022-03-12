from IntCode.IntCode import Comp
import re
import queue
from copy import copy
from itertools import combinations

def read_input():
    return list(map(int, [line.strip() for line in open('25.in')][0].split(',')))


def getRoom(output):
    try:
        pattern = r"\s*== ([\w\s-]*) =="
        m = re.findall(pattern, output)
        return m
    except AttributeError:
        return None


def get_directions(output):
    try:
        lines = output.strip().split('\n')
        lines = lines[lines.index('Doors here lead:'):]
        lines = lines[1:lines.index('')]
        return [line[2:] for line in lines]
    except ValueError:
        return None


def get_items(output):
    try:
        lines = output.strip().split('\n')
        lines = lines[lines.index('Items here:'):]
        lines = lines[1:lines.index('')]
        return [line[2:] for line in lines]
    except ValueError:
        return []


def path_to_unknown(world, room):
    q = queue.Queue()
    q.put((room, tuple()))
    visited = set()

    while not q.empty():
        node, path = q.get()
        if node in visited:
            continue
        visited.add(node)
        for d, n in world[node].items():
            if n is None:
                return path + (d,)
            else:
                q.put((n, path + (d,)))
    return tuple()

def part1():
    prog = read_input()
    comp = Comp(prog, input_buffer=[], mute=True)
    current_path = None
    inventory = []
    black_list = ['photons', 'molten lava', 'escape pod', 'infinite loop', 'giant electromagnet']
    world = {}
    while comp.execute():
        out = comp.pop_ascii()
        print(out)
        room = getRoom(out)[0] if getRoom(out) else room
        directions = get_directions(out) if get_directions(out) is not None else directions
        if room not in world and directions:
            world[room] = {d: None for d in directions}
        command = input('> ')
        if command == '':
            command = 'explore'
        if command == 'exit':
            return
        elif command == 'explore':
            path = path_to_unknown(world, room)
            while path:
                prev_room = room
                print(path, room)
                for d in path:
                    comp.feed_ascii(d, end='\n')
                    comp.execute()
                    out = comp.pop_ascii()
                    rooms = getRoom(out)
                    room = rooms[-1]
                    directions = get_directions(out)
                    items = get_items(out)
                    if room not in world:
                        print(out)
                        world[room] = {d: None for d in directions}
                        for item in items:
                            if item not in black_list:
                                comp.feed_ascii(f"take {item}", end='\n')
                                inventory.append(item)
                        comp.execute()
                        comp.pop_ascii()
                    world[prev_room][d] = room
                    prev_room = room
                    path = path_to_unknown(world, room)
                print(out)

        elif command == 'print':
            print(world)

        elif command == 'brute':
            all_items = copy(inventory)
            for num_items in range(len(all_items)):
                for comb in combinations(all_items, num_items):
                    for i in inventory:
                        if i not in comb:
                            comp.feed_ascii(f"drop {i}", end='\n')
                            inventory.remove(i)
                    for i in comb:
                        if i not in inventory:
                            comp.feed_ascii(f"take {i}", end='\n')
                            inventory.append(i)
                    comp.feed_ascii("west", end='\n')
                    comp.execute()
                    out = comp.pop_ascii()
                    rooms = getRoom(out)
                    if len(rooms) == 1:
                        print(out)

        else:
            comp.feed_ascii(command, end='\n')

def main():
    return part1()


if __name__ == '__main__':
    print(main())