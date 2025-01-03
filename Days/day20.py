grid = []
# (x, y, d)
curr_pos_og = (0, 0, 0)
end_pos = (0, 0)

with open("./Inputs/day20.txt", "r") as f:
    for iy, line in enumerate(f.read().strip().split("\n")):
        grid.append(list(line))
        for ix, x in enumerate(line):
            if x == "S":
                curr_pos_og = (ix, iy, 1)
                continue
            if x == "E":
                end_pos = (ix, iy)

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def getNeighbors(gn_grid, pos):
    n = []
    for i in range(4):
        p_c = (pos[0] + dir[i][0], pos[1] + dir[i][1], i), 1 #if i == pos[2] else 1001
        if gn_grid[p_c[0][1]][p_c[0][0]] == "#":
            continue
        n.append(p_c)
    
    return n

def buildPrevList(prevDict, curr):
    p = [tuple(curr)]
    while prevDict[tuple(curr)] != None:
        p.append(prevDict[tuple(curr)])
        curr = prevDict[curr]

    return p

visited = { (x, y, d): False for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }
costFromStart = { (x, y, d): float("inf") for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }
prev = { (x, y, d): None for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }

costFromStart[curr_pos_og] = 0

queue = [(curr_pos_og, costFromStart[curr_pos_og])]
while len(queue) > 0:
    curr_pos, curr_cost = queue.pop(0)

    if curr_pos[:2] == end_pos[:2]:
        break

    neighbors = getNeighbors(grid, curr_pos)

    for neighbor, cost in neighbors:
        if visited[neighbor] == True:
            continue
        visited[neighbor] = True
        costToNeighbor = costFromStart[curr_pos] + cost
        if costToNeighbor > costFromStart[neighbor]:
            continue
        costFromStart[neighbor] = costToNeighbor

        prev[neighbor] = curr_pos
    
        queue.append((neighbor, costToNeighbor))
        queue.sort(key = lambda nn: nn[1])

slowest_time = costFromStart[curr_pos]

times = []
for iy in range(1, len(grid) - 1):
    for ix in range(1, len(grid[iy]) - 1):
        print(f"{ix}, {iy}")
        if grid[iy][ix] in [".", "S", "E"]:
            continue

        og_pos_tile = grid[iy][ix]
        grid[iy][ix] = "."

        visited = { (x, y, d): False for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }
        costFromStart = { (x, y, d): float("inf") for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }
        prev = { (x, y, d): None for y in range(len(grid)) for x in range(len(grid[y])) for d in range(4) }

        costFromStart[curr_pos_og] = 0

        queue = [(curr_pos_og, costFromStart[curr_pos_og])]
        while len(queue) > 0:
            curr_pos, curr_cost = queue.pop(0)

            if curr_cost > slowest_time - 100:
                break

            if curr_pos[:2] == end_pos[:2]:
                break

            neighbors = getNeighbors(grid, curr_pos)

            for neighbor, cost in neighbors:
                if visited[neighbor] == True:
                    continue
                visited[neighbor] = True
                costToNeighbor = costFromStart[curr_pos] + cost
                if costToNeighbor > costFromStart[neighbor]:
                    continue
                costFromStart[neighbor] = costToNeighbor

                prev[neighbor] = curr_pos
            
                queue.append((neighbor, costToNeighbor))
                queue.sort(key = lambda nn: nn[1])

        grid[iy][ix] = og_pos_tile

        times.append(costFromStart[curr_pos])

fast_times = { slowest_time - t: times.count(t) for t in times if slowest_time - t >= 100 }

print(f"Answer 1: { sum(v for _k, v in fast_times.items()) }")
# print(f"Answer 2: { len({ tile[:2] for path in paths for tile in path }) }")