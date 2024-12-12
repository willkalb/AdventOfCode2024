with open("./Inputs/day10.txt", "r") as f:
    top_map = [ list(map(int, line)) for line in f.read().strip().split("\n") ]

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def inBounds(coord):
    return 0 <= coord[0] < len(top_map[0]) and 0 <= coord[1] < len(top_map)

def getUniqueEndpoints(x, y, num = 0):
    if top_map[y][x] == 9:
        return [(x, y)]

    next_positions = list(filter(inBounds, [ (x + d[0], y + d[1]) for d in dir ]))
    next_positions = list(filter(lambda c: top_map[c[1]][c[0]] == num + 1, next_positions))
    ends = set()
    for next_position in next_positions:
        eps = getUniqueEndpoints(next_position[0], next_position[1], num + 1)
        for ep in eps:
            ends.add(ep)

    return ends

def getUniquePathCount(x, y, num = 0):
    if top_map[y][x] == 9:
        return 1

    next_positions = list(filter(inBounds, [ (x + d[0], y + d[1]) for d in dir ]))
    next_positions = list(filter(lambda c: top_map[c[1]][c[0]] == num + 1, next_positions))
    
    return sum([ getUniquePathCount(n[0], n[1], num + 1) for n in next_positions ])

trailhead_endpoints = list()
trailhead_paths = list()
for y in range(len(top_map)):
    for x in range(len(top_map[y])):
        if top_map[y][x] != 0:
            continue

        trailhead_endpoints.append(((x, y), getUniqueEndpoints(x, y)))
        trailhead_paths.append(((x, y), getUniquePathCount(x, y)))

print(f"Answer 1: { len([ x for s in list(map(lambda t: t[1], trailhead_endpoints)) for x in s ]) }")
print(f"Answer 2: { sum([ p for p in list(map(lambda t: t[1], trailhead_paths)) ]) }")