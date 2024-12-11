def isSafe(list): 
    for i in range(0, len(list[:-1])):
        if abs(list[i] - list[i + 1]) > 3:
            return False
        if abs(list[i] - list[i + 1]) < 1:
            return False
        
        if i == 0:
            continue
        
        if list[i - 1] - list[i] < 0 and list[i] - list[i + 1] > 0:
            return False
        if list[i - 1] - list[i] > 0 and list[i] - list[i + 1] < 0:
            return False
        
    return True

def isSafe_Dampener(list):
    if isSafe(list):
        return True
    
    for i in range(0, len(list)):
        a = list[:i] + list[i + 1:]
        if isSafe(a):
            return True

    return False

reports = []
with open("./Inputs/day2.txt", "r") as f:
    reports = [ list(map(int, line.split())) for line in f ]

print(f"Answer 1: { len([ r for r in reports if isSafe(r) ]) }")
print(f"Answer 2: { len([ r for r in reports if isSafe_Dampener(r) ]) }")

