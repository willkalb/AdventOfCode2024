my_keypad = [
    [ "", "^", "A"],
    [ "<", "v", ">"]
]

robot_keypad_1 = [
    [ "", "^", "A"],
    [ "<", "v", ">"]
]
robot_keypad_1_pointer = [2, 0]

robot_keypad_2 = [
    [ "", "^", "A"],
    [ "<", "v", ">"]
]
robot_keypad_2_pointer = [2, 0]

door_keypad = [
    [ "7", "8", "9"],
    [ "4", "5", "6"],
    [ "1", "2", "3"],
    [ "", "0", "A"],
]
door_keypad_pointer = [2, 3]

def getDoorKeypadPosition(gdkp_keypad, gdkp_c):
    for y, row in enumerate(gdkp_keypad):
        for x, col in enumerate(row):
            if gdkp_c == col:
                return (x, y)
    
    raise Exception("OOPS")

def getRobotKeypadPosition(grkp_keypad, grkp_c):
    for y, row in enumerate(grkp_keypad):
        for x, col in enumerate(row):
            if grkp_c == col:
                return (x, y)
    
    raise Exception("OOPS")

def buildDoorPath(bdp_pointer, bdp_target, bdp_offset):
    path = []

    if bdp_pointer[1] == 3 and bdp_target[0] == 0:
        bdp_offset = (bdp_offset[0], bdp_offset[1] + 1)
        path.append("^")

        while bdp_offset[1] != 0:
            if bdp_offset[1] < 0:
                bdp_offset = (bdp_offset[0], bdp_offset[1] + 1)
                path.append("^")
            else:
                bdp_offset = (bdp_offset[0], bdp_offset[1] - 1)
                path.append("v")
        
    if bdp_pointer[0] == 0 and bdp_target[1] == 3:
        bdp_offset = (bdp_offset[0] - 1, bdp_offset[1])
        path.append(">")

    while bdp_offset[0] != 0:
        if bdp_offset[0] < 0:
            bdp_offset = (bdp_offset[0] + 1, bdp_offset[1])
            path.append("<")
        else:
            bdp_offset = (bdp_offset[0] - 1, bdp_offset[1])
            path.append(">")

    while bdp_offset[1] != 0:
        if bdp_offset[1] < 0:
            bdp_offset = (bdp_offset[0], bdp_offset[1] + 1)
            path.append("^")
        else:
            bdp_offset = (bdp_offset[0], bdp_offset[1] - 1)
            path.append("v")

    return path

def buildRobotKeypadPath(brkp_pointer, brkp_target, brkp_offset):
    path = []

    if brkp_pointer[1] == 0 and brkp_target[0] == 0:
        brkp_offset = (brkp_offset[0], brkp_offset[1] - 1)
        path.append("v")

        while brkp_offset[1] != 0:
            if brkp_offset[1] < 0:
                brkp_offset = (brkp_offset[0], brkp_offset[1] + 1)
                path.append("^")
            else:
                brkp_offset = (brkp_offset[0], brkp_offset[1] - 1)
                path.append("v")
        
    if brkp_pointer[0] == 0 and brkp_target[1] == 0:
        brkp_offset = (brkp_offset[0] - 1, brkp_offset[1])
        path.append(">")

    while brkp_offset[0] != 0:
        if brkp_offset[0] < 0:
            brkp_offset = (brkp_offset[0] + 1, brkp_offset[1])
            path.append("<")
        else:
            brkp_offset = (brkp_offset[0] - 1, brkp_offset[1])
            path.append(">")

    while brkp_offset[1] != 0:
        if brkp_offset[1] < 0:
            brkp_offset = (brkp_offset[0], brkp_offset[1] + 1)
            path.append("^")
        else:
            brkp_offset = (brkp_offset[0], brkp_offset[1] - 1)
            path.append("v")

    return path

def buildSequence(bs_code):
    global door_keypad_pointer
    global robot_keypad_2_pointer
    global robot_keypad_1_pointer

    sequence = []
    for c in bs_code:
        door_keypad_target_pos = getDoorKeypadPosition(door_keypad, c)
        door_keypad_target_offset = door_keypad_target_pos[0] - door_keypad_pointer[0], door_keypad_target_pos[1] - door_keypad_pointer[1]
        door_keypad_path = buildDoorPath(door_keypad_pointer, door_keypad_target_pos, door_keypad_target_offset) + ["A"]

        door_keypad_pointer = door_keypad_target_pos


        for dkp in door_keypad_path:
            robot_keypad_2_target_pos = getRobotKeypadPosition(robot_keypad_2, dkp)
            robot_keypad_2_target_offset = robot_keypad_2_target_pos[0] - robot_keypad_2_pointer[0], robot_keypad_2_target_pos[1] - robot_keypad_2_pointer[1]
            robot_keypad_2_path = buildRobotKeypadPath(robot_keypad_2_pointer, robot_keypad_2_target_pos, robot_keypad_2_target_offset) + ["A"]

            robot_keypad_2_pointer = robot_keypad_2_target_pos

            for rk2p in robot_keypad_2_path:
                robot_keypad_1_target_pos = getRobotKeypadPosition(robot_keypad_1, rk2p)
                robot_keypad_1_target_offset = robot_keypad_1_target_pos[0] - robot_keypad_1_pointer[0], robot_keypad_1_target_pos[1] - robot_keypad_1_pointer[1]
                robot_keypad_1_path = buildRobotKeypadPath(robot_keypad_1_pointer, robot_keypad_1_target_pos, robot_keypad_1_target_offset) + ["A"]

                robot_keypad_1_pointer = robot_keypad_1_target_pos

                sequence = sequence + robot_keypad_1_path

    return sequence

with open("./Inputs/day21.txt", "r") as f:
    codes = f.read().strip().split("\n")

sequences = { code: buildSequence(code) for code in codes }
for k in sequences:
    print("".join(sequences[k]))
complexities = { k: len(sequences[k]) * int("".join([ c for c in k if c.isdigit() ])) for k in sequences }

print(complexities)

print(f"Answer 1: { sum(complexities.values()) }")
# too high 244490

# print(f"Answer 2: { len({ tile[:2] for path in paths for tile in path }) }")