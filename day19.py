with open("./Inputs/day19.txt", "r") as f:
    lines = f.read().strip().split("\n")
    towels = lines[0].replace(" ", "").split(",")
    patterns = [ p for p in lines[2:]]

valid_pattern_cache = dict()
def isValid(iv_pattern):
    if iv_pattern in valid_pattern_cache:
        return valid_pattern_cache[iv_pattern]

    if iv_pattern in towels:
        valid_pattern_cache[iv_pattern] = True
        return True
    
    valid = False
    for t in towels:
        if valid == True:
            valid_pattern_cache[iv_pattern] = True
            return True
        if t == iv_pattern[:len(t)]:
            valid = isValid(iv_pattern[len(t):])
        
    
    valid_pattern_cache[iv_pattern] = False
    return False

arrangement_cache = dict()
def getPossibleArrangementsCount(gpa_pattern, depth = 0):
    if gpa_pattern in arrangement_cache:
        return arrangement_cache[gpa_pattern]
    
    arrangements = 0
    for t in towels:
        if t == gpa_pattern[:len(t)]:
            p_as = getPossibleArrangementsCount(gpa_pattern[len(t):], depth + 1)

            if p_as == 0 and gpa_pattern[len(t):] == "":
                arrangements += 1
                continue

            arrangements += p_as
    arrangement_cache[gpa_pattern] = arrangements

    return arrangements


valid_pattern_count = 0
arrangement_count = 0
for pattern in patterns:
    valid_pattern_count += isValid(pattern)
    arrangement_count += getPossibleArrangementsCount(pattern)

print(f"Answer 1: { valid_pattern_count }")
print(f"Answer 2: { arrangement_count }")