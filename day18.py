grid = [ [ "." for _ in range(71) ] for _ in range(71) ]
# (x, y, d)
curr_pos_og = (0, 0, 0)
end_pos = (70, 70)

corrupted_bytes = []

with open("./Inputs/day18.txt", "r") as f:
    for iy, line in enumerate(f.read().strip().split("\n")):
        x, y = list(map(int, line.split(",")))

        corrupted_bytes.append((x,y))

        if iy > 1024:
            continue

        grid[y][x] = "#"

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def inBounds(grid, pos):
    return 0 <= pos[0] < len(grid[0]) and 0 <= pos[1] < len(grid)

def getNeighbors(grid, pos):
    n = []
    for i in range(4):
        p = (pos[0] + dir[i][0], pos[1] + dir[i][1], i)
        if not inBounds(grid, p):
            continue
        if grid[p[1]][p[0]] == "#":
            continue
        n.append(p)
    
    return n

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

    for neighbor in neighbors:
        if visited[neighbor] == True:
            continue
        visited[neighbor] = True
                
        costToNeighbor = costFromStart[curr_pos] + 1
        if costToNeighbor > costFromStart[neighbor]:
            continue
        costFromStart[neighbor] = costToNeighbor

        prev[neighbor] = curr_pos
    
        queue.append((neighbor, costToNeighbor))
        queue.sort(key = lambda nn: nn[1])

shortestPath = costFromStart[curr_pos]

for cb in corrupted_bytes[1024:]:
    grid[cb[1]][cb[0]] = "#"

    curr_pos = curr_pos_og
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

        for neighbor in neighbors:
            if visited[neighbor] == True:
                continue
            visited[neighbor] = True
                    
            costToNeighbor = costFromStart[curr_pos] + 1
            if costToNeighbor > costFromStart[neighbor]:
                continue
            costFromStart[neighbor] = costToNeighbor

            prev[neighbor] = curr_pos
        
            queue.append((neighbor, costToNeighbor))
            queue.sort(key = lambda nn: nn[1])

    if curr_pos[:2] != (70, 70):
        break

print(f"Answer 1: { shortestPath }")
print(f"Answer 2: { cb }")