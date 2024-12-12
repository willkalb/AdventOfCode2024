with open("./Inputs/day9.txt", "r") as f:
    disk_map = list(map(int, f.read().strip()))

file_blocks = []
for i, length in enumerate(disk_map):
    id = i // 2 if i % 2 == 0 else -1

    file_blocks.extend([ int(id) for _ in range(length) ])

while -1 in file_blocks:
    if file_blocks[-1] == -1:
        del file_blocks[-1]
        continue

    file_blocks[file_blocks.index(-1)] = file_blocks[-1]
    del file_blocks[-1]

print(f"Answer 1: { sum( i * id for i, id in enumerate(file_blocks) ) }")
# print(f"Answer 2: { len(set(map(lambda x: (x[0], x[1]), resonate_antinodes))) }")