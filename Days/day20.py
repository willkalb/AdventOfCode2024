grid = []
# (x, y)
curr_pos = (0, 0)
end_pos = (0, 0)

with open("./Inputs/day20.txt", "r") as f:
    for iy, line in enumerate(f.read().strip().split("\n")):
        grid.append(list(line))
        for ix, x in enumerate(line):
            if x == "S":
                curr_pos = (ix, iy)
                continue
            if x == "E":
                end_pos = (ix, iy)

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def getNeighbors(gn_grid, pos):
    n = []
    for i in range(4):
        p_c = (pos[0] + dir[i][0], pos[1] + dir[i][1]), 1
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

def getPhasedTilePositions(tile_pos, phase_dur):
    phased_tiles = list()
    for p in range(1, phase_dur):
        phased_tiles.append((tile_pos[0] - (phase_dur - 1 - p), tile_pos[1] - p))
        phased_tiles.append((tile_pos[0] + p, tile_pos[1] + (phase_dur - 1 - p)))
        phased_tiles.append((tile_pos[0] + (phase_dur - 1 - p), tile_pos[1] + p))
        phased_tiles.append((tile_pos[0] - p, tile_pos[1] - (phase_dur - 1 - p)))

    return list(filter(lambda t: 0 < t[0] < len(grid[0]) - 1 and 0 < t[1] < len(grid) - 1, phased_tiles))

def findShortestPath(fsp_start_pos, fsp_end_pos, fsp_grid):
    visited = { (x, y): False for y in range(len(fsp_grid)) for x in range(len(fsp_grid[y])) }
    costFromStart = { (x, y): float("inf") for y in range(len(fsp_grid)) for x in range(len(fsp_grid[y])) }
    prev = { (x, y): None for y in range(len(fsp_grid)) for x in range(len(fsp_grid[y])) }

    costFromStart[fsp_start_pos] = 0

    queue = [(fsp_start_pos, costFromStart[fsp_start_pos])]
    while len(queue) > 0:
        curr_pos, curr_cost = queue.pop(0)

        if curr_pos == fsp_end_pos:
            break

        neighbors = getNeighbors(fsp_grid, curr_pos)

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

    path = buildPrevList(prev, curr_pos)
    path.reverse()

    return path

path = findShortestPath(curr_pos, end_pos, grid)

shorter_paths_count = 0

phase_duration = 2
for i, tile in enumerate(path):
    if i % 500 == 0:
        print(i)

    phased_tiles = getPhasedTilePositions(tile, phase_duration)
    og_grid_tiles = { tile: grid[tile[1]][tile[0]] for tile in phased_tiles }
    for pt in phased_tiles:
        if pt in path[:i]:
            continue

        grid[pt[1]][pt[0]] = "."

        new_path = findShortestPath(pt, end_pos, grid)
        new_path = path[:i + 1] + new_path

        if len(new_path) <= len(path) - 40:
            shorter_paths_count += 1

        grid[pt[1]][pt[0]] = og_grid_tiles[pt]

print(f"Answer 1: { shorter_paths_count }")
# print(f"Answer 2: { len({ tile[:2] for path in paths for tile in path }) }")