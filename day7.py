with open("./Inputs/day7.txt", "r") as f:
    equations = []
    for line in f:
        val, operand = line.split(":")
        equations.append((int(val), list(map(int, operand.strip().split(" ")))))

def reduce_2_operator(operands):
    a, b = operands[0], operands[1]
    r = operands[2:]

    c1 = [a + b] + r
    c2 = [a * b] + r

    return [c1, c2]

def reduce_3_operator(operands):
    a, b = operands[0], operands[1]
    r = operands[2:]

    c1 = [a + b] + r
    c2 = [a * b] + r
    c3 = [int(str(a) + str(b))] + r

    return [c1, c2, c3]

two_operator_correct_equations_sum = 0
for equation in equations:
    possible_equations = [equation[1]]

    while len(possible_equations) > 0:
        found = False
        for c in reduce_2_operator(possible_equations[0]):
            if found:
                break
            if len(c) > 1:
                possible_equations.append(c)
                continue

            if c[0] == equation[0]:
                found = True
                two_operator_correct_equations_sum = two_operator_correct_equations_sum + c[0]
                break
        if found:
            break
        possible_equations = possible_equations[1:]
        possible_equations.sort(key = lambda e: len(e))
    
three_operator_correct_equations_sum = 0
for equation in equations:
    possible_equations = [equation[1]]

    while len(possible_equations) > 0:
        found = False
        for c in reduce_3_operator(possible_equations[0]):
            if found:
                break
            if len(c) > 1:
                possible_equations.append(c)
                continue

            if c[0] == equation[0]:
                found = True
                three_operator_correct_equations_sum = three_operator_correct_equations_sum + c[0]
                break
        if found:
            break
        possible_equations = possible_equations[1:]
        possible_equations.sort(key = lambda e: len(e))
    

print(f"Answer 1: { two_operator_correct_equations_sum }")
print(f"Answer 2: { three_operator_correct_equations_sum }")