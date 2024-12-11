with open("./Inputs/day6.txt", "r") as f:
    patrol_map = [list(line) for line in f.read().strip().split("\n")]

d = [[0, -1], [1, 0], [0, 1], [-1, 0]]

print([ c for c in [ row for row in patrol_map ] if c == "^" ])

starting_pos = (69, 44)
cols = len(patrol_map[0])
rows = len(patrol_map)

def createsLoop(x, y):
    if patrol_map[y][x] == "#":
        return 0
    
    patrol_map[y][x] = "#"
    
    t_guard_pos = starting_pos
    t_guard_dir = 0
    t_guard_seen = set()

    while True:
        if (t_guard_pos[0], t_guard_pos[1], t_guard_dir) in t_guard_seen:
            patrol_map[y][x] = "."
            return 1
        
        t_guard_seen.add((t_guard_pos[0], t_guard_pos[1], t_guard_dir))
        next_pos = (t_guard_pos[0] + d[t_guard_dir][0], t_guard_pos[1] + d[t_guard_dir][1])

        if not (0 <= next_pos[0] < cols and 0 <= next_pos[1] < rows):
            patrol_map[y][x] = "."
            return 0
        
        if patrol_map[next_pos[1]][next_pos[0]] == "#":
            t_guard_dir = (t_guard_dir + 1) % 4
            continue

        t_guard_pos = next_pos

guard_pos = starting_pos
guard_dir = 0
guard_seen = set()
while True:
    guard_seen.add(guard_pos)
    next_pos = (guard_pos[0] + d[guard_dir][0], guard_pos[1] + d[guard_dir][1])

    if not (0 <= next_pos[0] < cols and 0 <= next_pos[1] < rows):
        break

    if patrol_map[next_pos[1]][next_pos[0]] == "#":
        guard_dir = (guard_dir + 1) % 4
        continue

    guard_pos = next_pos

obstacle_count = 0
for x, y in guard_seen:
    if x == starting_pos[0] and y == starting_pos[1]:
        continue

    obstacle_count = obstacle_count + createsLoop(x, y)

print(f"Answer 1: { len(set(map(lambda t: (t[0], t[1]), guard_seen))) }")
print(f"Answer 2: { obstacle_count }")