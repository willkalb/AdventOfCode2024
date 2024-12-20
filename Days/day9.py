with open("./Inputs/day9.txt", "r") as f:
    disk_map = list(map(int, f.read().strip()))

og_file_blocks = []
for i, length in enumerate(disk_map):
    id = i // 2 if i % 2 == 0 else -1

    og_file_blocks.extend([ int(id) for _ in range(length) ])

p1_file_block = og_file_blocks[:]
while -1 in p1_file_block:
    if p1_file_block[-1] == -1:
        del p1_file_block[-1]
        continue

    p1_file_block[p1_file_block.index(-1)] = p1_file_block[-1]
    del p1_file_block[-1]

p2_file_block = og_file_blocks[:]
for id in range(p2_file_block[-1], -1, -1):
    i_file_start = p2_file_block.index(id)
    i_file_end = i_file_start + disk_map[id * 2]

    file_block_spaces = p2_file_block[i_file_start:i_file_end]

    for i_blank_start in range(0, i_file_start):
        if p2_file_block[i_blank_start] != -1:
            continue

        i_blank_end = i_blank_start + disk_map[id * 2]
        if p2_file_block[i_blank_start:i_blank_end] == [ -1 for _ in range(disk_map[id * 2])]:
            p2_file_block[i_blank_start:i_blank_end], p2_file_block[i_file_start:i_file_end] = file_block_spaces, [ -1 for _ in range(disk_map[id * 2])]
            break

print(f"Answer 1: { sum( i * id for i, id in enumerate(p1_file_block) ) }")
print(f"Answer 2: { sum( i * id for i, id in enumerate(p2_file_block) if id != -1 ) }")