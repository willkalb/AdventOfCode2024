with open("./Inputs/day8.txt", "r") as f:
    antenna_map = [ list(line) for line in f.read().strip().split("\n") ]

rows = len(antenna_map)
cols = len(antenna_map[0])

def getAntennasWithSameFrequency(ox, oy):
    antennas = []
    for y in range(oy, rows):
        for x in range(cols):
            if y <= oy and x <= ox:
                continue
            if antenna_map[oy][ox] != antenna_map[y][x]:
                continue

            antennas.append([x, y])

    return antennas

def buildAntinodes(a1, a2):
    slope = (a1[0] - a2[0], a1[1] - a2[1])
    an1 = (a1[0] + slope[0], a1[1] + slope[1])
    an2 = (a2[0] + -slope[0], a2[1] + -slope[1])

    return [an1, an2]

def buildResonateAntinodes(a1, a2):
    slope = (a1[0] - a2[0], a1[1] - a2[1])

    ans1 = [ a1 ]
    next_an = (a1[0] + slope[0], a1[1] + slope[1])
    while inBounds(next_an):
        ans1.append(next_an)
        next_an = (next_an[0] + slope[0], next_an[1] + slope[1])

    ans2 = [ a2 ]
    next_an = (a2[0] + -slope[0], a2[1] + -slope[1])
    while inBounds(next_an):
        ans2.append(next_an)
        next_an = (next_an[0] + -slope[0], next_an[1] + -slope[1])

    return [*ans1, *ans2]

def inBounds(coord):
    return 0 <= coord[0] < cols and 0 <= coord[1] < rows
    
antinodes = []
resonate_antinodes = []
for y in range(rows):
    for x in range(cols):
        if antenna_map[y][x] == ".":
            continue
        if antenna_map[y][x] == "#":
            continue

        matching_antennas = getAntennasWithSameFrequency(x, y)
        for matching_antenna in matching_antennas:
            antenna_antinodes = list(filter(inBounds, buildAntinodes((x, y), matching_antenna)))
            antinodes = antinodes + list(map(lambda aa: (*aa, antenna_map[y][x]), antenna_antinodes))

            antenna_resonate_antinodes = list(filter(inBounds, buildResonateAntinodes((x, y), matching_antenna)))
            resonate_antinodes = resonate_antinodes + list(map(lambda aa: (*aa, antenna_map[y][x]), antenna_resonate_antinodes))

print(f"Answer 1: { len(set(map(lambda x: (x[0], x[1]), antinodes))) }")
print(f"Answer 2: { len(set(map(lambda x: (x[0], x[1]), resonate_antinodes))) }")