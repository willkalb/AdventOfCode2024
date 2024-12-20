with open("./Inputs/day11.txt", "r") as f:
    og_stones = [ int(line) for line in f.read().strip().split(" ") ]

def getChildren(parent_stone):
    if parent_stone == 0:
        return [1]
    if len(str_stone := str(parent_stone)) % 2 == 0:
        return [int(str_stone[0:len(str_stone) // 2]), int(str_stone[len(str_stone) // 2:])]
    return [parent_stone * 2024]

stone_cache = {}
def getChildrenLength(blinks, stone, gen = 0):
    if blinks == gen:
        return 1
    
    if (stone, gen) in stone_cache:
        return stone_cache[(stone, gen)]

    child_len = sum([ getChildrenLength(blinks, c, gen + 1) for c in getChildren(stone) ])

    stone_cache[(stone, gen)] = child_len

    return child_len

stones_len_p1 = 0
for stone in og_stones:
    stones_len_p1 += getChildrenLength(25, stone)

stone_cache = {}
stones_len_p2 = 0
for stone in og_stones:
    stones_len_p2 += getChildrenLength(75, stone)

print(f"Answer 1: { stones_len_p1 }")
print(f"Answer 2: { stones_len_p2 }")