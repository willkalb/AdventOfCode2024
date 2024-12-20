machines = []

with open("./Inputs/day13.txt", "r") as f:
    curr_config = dict()
    curr_prize = ()
    for line in f.read().split("\n"):
        if line[:8] == "Button A":
            x_start = line.find("X+") + 2
            x_end = line.find(",")
            y_start = line.find("Y+") + 2
            curr_config["A"] = (int(line[x_start:x_end]), int(line[y_start:]))
            continue
        if line[:8] == "Button B":
            x_start = line.find("X+") + 2
            x_end = line.find(",")
            y_start = line.find("Y+") + 2
            curr_config["B"] = (int(line[x_start:x_end]), int(line[y_start:]))
            continue
        if line[:5] == "Prize":
            x_start = line.find("X=") + 2
            x_end = line.find(",")
            y_start = line.find("Y=") + 2
            curr_prize = (int(line[x_start:x_end]), int(line[y_start:]))
            continue

        machines.append((curr_config, curr_prize))
        curr_config = dict()
        curr_prize = ()

    machines.append((curr_config, curr_prize))

m1 = machines.copy()
for i, machine in enumerate(m1):
    Ap = 0                  # Button A presses
    Ax = machine[0]["A"][0] # Button A x coord difference
    Ay = machine[0]["A"][1] # Button A y coord difference
    Bp = 0                  # Button B presses
    Bx = machine[0]["B"][0] # Button B x coord difference
    By = machine[0]["B"][1] # Button B y coord difference
    Px = machine[1][0]      # Prize x coord
    Py = machine[1][1]      # Prize y coord

    # Py = (Ap * Ay) + (Bp * By)
    # Px = (Ap * Ax) + (Bp * Bx)

    # substitution for Ap
    # Py = (Ap * Ay) + (Bp * By)
    # Py - (Bp * By) = (Ap * Ay)
    # (Ap * Ay) = Py - (Bp * By)
    # Ap = (Py - (Bp * By)) / Ay
    
    # substitution for Bp
    # Px = (Ap * Ax) + (Bp * Bx)
    # Px - (Ap * Ax) = (Bp * Bx)
    # (Bp * Bx) = Px - (Ap * Ax)
    # Bp = (Px - (Ap * Ax)) / Bx

    # substitute
    # Py = (Ap * Ay) + (((Px - (Ap * Ax)) / Bx) * By)
    # Px = (((Py - (Bp * By)) / Ay) * Ax) + (Bp * Bx)

    # solve for button press
    # Py = (((Px - (Ap * Ax)) / Bx) * By) + (Ap * Ay)
    # Py = (((Px * By) - ((Ap * Ax) * By)) / Bx) + (Ap * Ay)
    # Py - (Ap * Ay) = ((Px * By) - ((Ap * Ax) * By)) / Bx
    # (Py * Bx) - ((Ap * Ay) * Bx) = (Px * By) - ((Ap * Ax) * By)
    # 0 - (Ap * Ay * Bx) + (Ap * Ax * By) = (Px * By) - (Py * Bx)
    # (Ap * Ax * By) - (Ap * Ay * Bx) = (Px * By) - (Py * Bx)
    # Ap * ((Ax * By) - (Ay * Bx)) = (Px * By) - (Py * Bx)
    # Ap = ((Px * By) - (Py * Bx)) / ((Ax * By) - (Ay * Bx))

    # Px = (((Py - (Bp * By)) / Ay) * Ax) + (Bp * Bx)
    # Px = (((Py * Ax) - ((Bp * By) * Ax)) / Ay) + (Bp * Bx)
    # Px - (Bp * Bx) = ((Py * Ax) - ((Bp * By) * Ax)) / Ay
    # (Px * Ay) - ((Bp * Bx) * Ay) = (Py * Ax) - ((Bp * By) * Ax)
    # 0 - (Bp * Bx * Ay) + (Bp * By * Ax) = (Py * Ax) - (Px * Ay)
    # (Bp * By * Ax) - (Bp * Bx * Ay) = (Py * Ax) - (Px * Ay)
    # Bp * ((By * Ax) - (Bx * Ay)) = (Py * Ax) - (Px * Ay)
    # Bp = ((Py * Ax) - (Px * Ay)) / ((By * Ax) - (Bx * Ay))

    Ap = ((Px * By) - (Py * Bx)) / ((Ax * By) - (Ay * Bx))
    Bp = ((Py * Ax) - (Px * Ay)) / ((By * Ax) - (Bx * Ay))

    if Ap != int(Ap) or Bp != int(Bp):
        m1[i] = (machine[0], machine[1], float("inf"))
        continue

    if Ap > 100 or Ap > 100:
        m1[i] = (machine[0], machine[1], float("inf"))
        continue

    tokens = int((3 * Ap) + Bp)

    m1[i] = (machine[0], machine[1], tokens)

    pass

m2 = machines.copy()
for i, machine in enumerate(m2):
    Ap = 0
    Ax = machine[0]["A"][0]
    Ay = machine[0]["A"][1]
    Bp = 0
    Bx = machine[0]["B"][0]
    By = machine[0]["B"][1]
    Px = machine[1][0] + 10000000000000
    Py = machine[1][1] + 10000000000000

    Ap = ((Px * By) - (Py * Bx)) / ((Ax * By) - (Ay * Bx))
    Bp = ((Py * Ax) - (Px * Ay)) / ((By * Ax) - (Bx * Ay))

    if Ap != int(Ap) or Bp != int(Bp):
        m2[i] = (machine[0], machine[1], float("inf"))
        continue

    tokens = int((3 * Ap) + Bp)

    m2[i] = (machine[0], machine[1], tokens)

    pass

print(f"Answer 1: { sum([ m[2] for m in m1 if m[2] != float("inf") ]) }")
print(f"Answer 2: { sum([ m[2] for m in m2 if m[2] != float("inf") ]) }")