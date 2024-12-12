with open("./Inputs/day9.txt", "r") as f:
    disk_map = list(map(int, f.read()))

file_blocks = []
for i, num in enumerate(disk_map):
    id = i / 2
    if id != int(id):
        id = -1

    file_blocks.extend([ int(id) for _ in range(num) ])

free_space_blocks = file_blocks.count(-1)
while True:
    while file_blocks[-1:][0] == -1:
        del file_blocks[-1]
        free_space_blocks -= 1

    if free_space_blocks == 0:
        break

    file_blocks[next(i for i, id in enumerate(file_blocks) if id == -1)] = file_blocks[-1:][0]
    del file_blocks[-1]
    free_space_blocks -= 1

# file_blocks = file_blocks + ([-1] * free_space_blocks)

print(f"Answer 1: { sum([ i * id for i, id in enumerate(file_blocks) ]) }")
# 5001859401903 too low
# 6412389511995 too high
# print(f"Answer 2: { len(set(map(lambda x: (x[0], x[1]), resonate_antinodes))) }")