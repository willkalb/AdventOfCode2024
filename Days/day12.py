with open("./Inputs/day12.txt", "r") as f:
    garden = [ list(line) for line in f.read().strip().split("\n") ]

dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cc = [(0, 0), (1, 0), (1, 1), (0, 1)]
inRegion = []

def inBounds(coord):
    return 0 <= coord[0] < len(garden[0]) and 0 <= coord[1] < len(garden)

def getPlantsInRegion(plantType, c, local_region):
    if c in inRegion:
        return []
        
    inRegion.append(c)
    local_region.append(c)

    neighbors = [ (c[0] + d[0], c[1] + d[1]) for d in dir ]
    for n in neighbors:
        if not inBounds(n):
            continue
        if garden[n[1]][n[0]] != plantType:
            continue
        if n in inRegion:
            continue
        
        local_region = getPlantsInRegion(plantType, n, local_region)

    return local_region

def getPerimeter(region):
    plots_visited = []
    fence_count = 0
    for plot in region:
        plots_visited.append(plot)
        neighbors = [ (plot[0] + d[0], plot[1] + d[1]) for d in dir if (plot[0] + d[0], plot[1] + d[1]) in region ]
        fence_count += 4 - len(neighbors)

    return fence_count

def getSides(region):
    region_plot_coords = [ (p[0] + cc[i][0], p[1] + cc[i][1]) for i in range(4) for p in region ]
    unique_plot_coords = set(region_plot_coords)
    corners = 0
    for upc in unique_plot_coords:
        unique_plot_coord_count = region_plot_coords.count(upc)

        if unique_plot_coord_count == 4:
            continue

        if unique_plot_coord_count % 2 == 1:
            corners += 1
            continue

        plot_neighbors = []
        for p in region:
            plot_coords = [ p for i in range(4) if upc == (p[0] + cc[i][0], p[1] + cc[i][1]) ]

            if len(plot_coords) > 0:
                plot_neighbors.extend(plot_coords)

        if plot_neighbors[0][0] != plot_neighbors[1][0] and plot_neighbors[0][1] != plot_neighbors[1][1]:
            corners += 2
            continue

    # corners == sides
    return corners

garden_regions = []
for y in range(len(garden)):
    for x in range(len(garden[y])):
        if (x, y) in inRegion:
            continue

        garden_regions.append((garden[y][x], getPlantsInRegion(garden[y][x], (x, y), [])))

garden_specs = []
for plant, region in garden_regions:
    garden_specs.append((len(region), getPerimeter(region), getSides(region)))

print(f"Answer 1: { sum([ s[0] * s[1] for s in garden_specs ]) }")
print(f"Answer 2: { sum([ s[0] * s[2] for s in garden_specs ]) }")