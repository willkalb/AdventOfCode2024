registers_og = dict()
program = []
output = []

def combo(operand):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    
    return None

def adv(curr_i, operand):
    operand = combo(operand)
    registers["A"] = registers["A"] // 2**operand

    return curr_i + 2

def bxl(curr_i, operand):
    registers["B"] = registers["B"] ^ operand

    return curr_i + 2

def bst(curr_i, operand):
    operand = combo(operand)
    registers["B"] = operand % 8

    return curr_i + 2

def jnz(curr_i, operand):
    if registers["A"] == 0:
        return curr_i + 2
    
    return operand

def bxc(curr_i, _operand):
    registers["B"] = registers["B"] ^ registers["C"]

    return curr_i + 2

def out(curr_i, operand):
    operand = combo(operand)
    output.append(str(operand % 8))

    return curr_i + 2

def bdv(curr_i, operand):
    operand = combo(operand)
    registers["B"] = registers["A"] // 2**operand

    return curr_i + 2

def cdv(curr_i, operand):
    operand = combo(operand)
    registers["C"] = registers["A"] // 2**operand

    return curr_i + 2

instructions = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

with open("./Inputs/day17.txt", "r") as f:
    for iy, line in enumerate(f.read().strip().split("\n")):
        if line[:10] == "Register A":
            registers_og["A"] = int(line[12:])
            continue
        if line[:10] == "Register B":
            registers_og["B"] = int(line[12:])
            continue
        if line[:10] == "Register C":
            registers_og["C"] = int(line[12:])
            continue
        if line[:7] == "Program":
            program = [ int(n) for n in line[9:].split(",") ]
            continue

registers = registers_og.copy()
i = 0
while i < len(program):
    i = instructions[program[i]](i, program[i + 1])
output_1 = output[:]

registers = registers_og.copy()
output_og = output[:]
a = 1
output = []

ii = -1

while -len(program) <= ii:
    registers["A"] = a
    output = []
    i = 0
    while i < len(program):
        i = instructions[program[i]](i, program[i + 1])

    if list(map(int,output)) == program:
        break

    if list(map(int,output[ii:])) == program[ii:]:
        a *= 8
        ii -= 1
        continue
    
    a += 1

print(f"Answer 1: { ",".join(output_1) }")
print(f"Answer 2: { a }")