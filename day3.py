import re

def exec(mul):
    pivot = mul.find(",")
    n1 = mul[4:pivot]
    n2 = mul[pivot + 1:-1]

    return int(n1) * int(n2)

def parse(text, p2 = False):
    instructions, instructions_2 = [], []
    do = True
    for i in range(0, len(text)):
        searching = text[i:i + 12]

        if searching[:4] == "do()":
            do = True
        if searching[:7] == "don't()":
            do = False

        if searching[:4] != "mul(":
            continue

        match = re.search(r"mul\(\d{1,3},\d{1,3}\)", searching)
        
        if match == None:
            continue
        
        instructions.append(match.group())

        if not do:
            continue

        instructions_2.append(match.group())
    
    return [ instructions, instructions_2 ]

str_instruction = ""
with open("./Inputs/day3.txt", "r") as f:
    str_instruction = f.read()

[ inst, inst_2 ] = parse(str_instruction)
print(f"Answer 1: { sum(list(map(lambda m: exec(m), inst))) }")
print(f"Answer 2: { sum(list(map(lambda m: exec(m), inst_2))) }")
