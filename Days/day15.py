from copy import deepcopy

warehouse_og = []
moves = []
curr_pos_og = []

dir = { "^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

with open("./Inputs/day15.txt", "r") as f:
    for i, line in enumerate(f.read().split("\n")):
        if len(line) == 0:
            continue

        if "#" in line:
            warehouse_og.append([*line])
            if "@" in line:
                curr_pos_og = [line.find("@"), i]
        else:
            moves.extend([*line])

curr_pos_1 = curr_pos_og.copy()
warehouse_1 = deepcopy(warehouse_og)

curr_pos_2 = (curr_pos_og[0] * 2, curr_pos_og[1])
warehouse_2 = []

for iy in range(len(warehouse_og)):
    row = []
    for ix in range(len(warehouse_og[iy])):
        if warehouse_og[iy][ix] == "#":
            row.extend(["#", "#"])
            continue
        if warehouse_og[iy][ix] == "O":
            row.extend(["[", "]"])
            continue
        if warehouse_og[iy][ix] == ".":
            row.extend([".", "."])
            continue
        if warehouse_og[iy][ix] == "@":
            row.extend(["@", "."])
            continue
    warehouse_2.append(row)

def move_1(warehouse, curr_pos, d):
    next_p = [curr_pos[0] + dir[d][0], curr_pos[1] + dir[d][1]]

    if warehouse[next_p[1]][next_p[0]] == ".":
        warehouse[curr_pos[1]][curr_pos[0]], warehouse[next_p[1]][next_p[0]] = warehouse[next_p[1]][next_p[0]], warehouse[curr_pos[1]][curr_pos[0]]
        curr_pos = [curr_pos[0] + dir[d][0], curr_pos[1] + dir[d][1]]
        return warehouse, curr_pos
    
    pos_p = next_p.copy()
    while warehouse[pos_p[1]][pos_p[0]] == "O":
        pos_p = [pos_p[0] + dir[d][0], pos_p[1] + dir[d][1]]
    
    if warehouse[pos_p[1]][pos_p[0]] == ".":
        warehouse[next_p[1]][next_p[0]], warehouse[pos_p[1]][pos_p[0]] = warehouse[pos_p[1]][pos_p[0]], warehouse[next_p[1]][next_p[0]]
        warehouse[curr_pos[1]][curr_pos[0]], warehouse[next_p[1]][next_p[0]] = warehouse[next_p[1]][next_p[0]], warehouse[curr_pos[1]][curr_pos[0]]
        curr_pos = [curr_pos[0] + dir[d][0], curr_pos[1] + dir[d][1]]

    return warehouse, curr_pos

def getBoxesMoving_Up(warehouse, curr_pos, boxes):
    next_p = [curr_pos[0], curr_pos[1] + dir["^"][1]]
    
    if  warehouse[next_p[1]][next_p[0]] in [".", "#"]:
        return boxes

    box_l = (next_p[0], next_p[1])
    box_r = (next_p[0], next_p[1])

    if warehouse[next_p[1]][next_p[0]] == "[":
        box_r = (box_r[0] + 1, box_l[1])
    if warehouse[next_p[1]][next_p[0]] == "]":
        box_l = (box_l[0] - 1, box_l[1])

    if warehouse[box_l[1] + dir["^"][1]][box_l[0]] == "#" or warehouse[box_r[1] + dir["^"][1]][box_r[0]] == "#":
        boxes = set()
        return boxes
    
    boxes.add((box_l, box_r))

    if warehouse[box_l[1] + dir["^"][1]][box_l[0]] == "." and warehouse[box_r[1] + dir["^"][1]][box_r[0]] == ".":
        return boxes
    
    boxes = getBoxesMoving_Up(warehouse, box_r, boxes)
    if len(boxes) == 0:
        return set()
    boxes = getBoxesMoving_Up(warehouse, box_l, boxes)

    return boxes

def getBoxesMoving_Right(warehouse, curr_pos, boxes):
    next_p = [curr_pos[0] + dir[">"][0], curr_pos[1] + dir[">"][1]]

    if warehouse_2[next_p[1]][next_p[0]] == "#":
        return set()

    if warehouse_2[next_p[1]][next_p[0]] == ".":
        return boxes

    box_l = (next_p[0], next_p[1])
    box_r = (next_p[0] + dir[">"][0], next_p[1])

    if warehouse[box_l[1] + dir[">"][1]][box_l[0] + dir[">"][0]] == "#":
        boxes = set()
        return boxes
    
    boxes.add((box_l, box_r))

    if warehouse[box_l[1] + dir[">"][1]][box_l[0] + dir[">"][0]] == ".":
        return boxes
    
    boxes = getBoxesMoving_Right(warehouse, box_r, boxes)

    return boxes

def getBoxesMoving_Down(warehouse, curr_pos, boxes):
    next_p = [curr_pos[0], curr_pos[1] + dir["v"][1]]
    
    if warehouse[next_p[1]][next_p[0]] in [".", "#"]:
        return boxes

    box_l = (next_p[0], next_p[1])
    box_r = (next_p[0], next_p[1])

    if warehouse[next_p[1]][next_p[0]] == "[":
        box_r = (box_r[0] + 1, box_l[1])
    if warehouse[next_p[1]][next_p[0]] == "]":
        box_l = (box_l[0] - 1, box_l[1])

    if warehouse[box_l[1] + dir["v"][1]][box_l[0]] == "#" or warehouse[box_r[1] + dir["v"][1]][box_r[0]] == "#":
        boxes = set()
        return boxes
    
    boxes.add((box_l, box_r))

    if warehouse[box_l[1] + dir["v"][1]][box_l[0]] == "." and warehouse[box_r[1] + dir["v"][1]][box_r[0]] == ".":
        return boxes
    
    boxes = getBoxesMoving_Down(warehouse, box_r, boxes)
    if len(boxes) == 0:
        return set()
    boxes = getBoxesMoving_Down(warehouse, box_l, boxes)

    return boxes

def getBoxesMoving_Left(warehouse, curr_pos, boxes):
    next_p = [curr_pos[0] + dir["<"][0], curr_pos[1] + dir["<"][1]]

    if warehouse_2[next_p[1]][next_p[0]] == "#":
        return set()

    if warehouse_2[next_p[1]][next_p[0]] == ".":
        return boxes

    box_l = (next_p[0] + dir["<"][0], next_p[1])
    box_r = (next_p[0], next_p[1])

    if warehouse[box_l[1] + dir["<"][1]][box_l[0] + dir["<"][0]] == "#":
        boxes = set()
        return boxes
    
    boxes.add((box_l, box_r))

    if warehouse[box_l[1] + dir["<"][1]][box_l[0] + dir["<"][0]] == ".":
        return boxes
    
    boxes = getBoxesMoving_Left(warehouse, box_l, boxes)

    return boxes

def move_2(warehouse, curr_pos, d):
    boxes_moving = set()
    if d == "^":
        boxes_moving = getBoxesMoving_Up(warehouse_2, curr_pos_2, set())
    elif d == ">":
        boxes_moving = getBoxesMoving_Right(warehouse_2, curr_pos_2, set())
    elif d == "v":
        boxes_moving = getBoxesMoving_Down(warehouse_2, curr_pos_2, set())
    elif d == "<":
        boxes_moving = getBoxesMoving_Left(warehouse_2, curr_pos_2, set())

    new_boxes_pos = set()
    for box in boxes_moving:
        new_boxes_pos.add(((box[0][0] + dir[d][0], box[0][1] + dir[d][1]), (box[1][0] + dir[d][0], box[1][1] + dir[d][1])))

    warehouse[curr_pos[1]][curr_pos[0]] = "."
    for box in boxes_moving:
        warehouse[box[0][1]][box[0][0]] = "."
        warehouse[box[1][1]][box[1][0]] = "."

    if warehouse[curr_pos[1] + dir[d][1]][curr_pos[0] + dir[d][0]] == ".":
        curr_pos = (curr_pos[0] + dir[d][0], curr_pos[1] + dir[d][1])

    warehouse[curr_pos[1]][curr_pos[0]] = "@"
    for box in new_boxes_pos:
        warehouse[box[0][1]][box[0][0]] = "["
        warehouse[box[1][1]][box[1][0]] = "]"

    return (warehouse, curr_pos)

for move in moves:
    warehouse_1, curr_pos_1 = move_1(warehouse_1, curr_pos_1, move)
    warehouse_2, curr_pos_2 = move_2(warehouse_2, curr_pos_2, move)

print(f"Answer 1: { sum((100 * iy) + ix for iy, y in enumerate(warehouse_1) for ix, x in enumerate(y) if warehouse_1[iy][ix] == "O") }")
print(f"Answer 2: { sum((100 * min(iy - 0, len(y) - iy + 1)) + ix for iy, y in enumerate(warehouse_2) for ix, x in enumerate(y) if warehouse_2[iy][ix] == "[") }")