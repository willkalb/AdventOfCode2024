with open("./Inputs/day19.txt", "r") as f:
    lines = f.read().strip().split("\n")
    towels = lines[0].replace(" ", "").split(",")
    patterns = [ p for p in lines[2:]]

arrangement_cache = dict()
def getPossibleArrangementsCount(gpa_pattern):
    if gpa_pattern in arrangement_cache:
        return arrangement_cache[gpa_pattern]
    
    if len(gpa_pattern) == 0: 
        return 1
    
    arrangements = 0
    for t in towels:
        if t == gpa_pattern[:len(t)]:
            arrangements += getPossibleArrangementsCount(gpa_pattern[len(t):])
            
    arrangement_cache[gpa_pattern] = arrangements

    return arrangements


valid_pattern_count = 0
arrangement_count = 0
for pattern in patterns:
    poss_arr_count = getPossibleArrangementsCount(pattern)
    valid_pattern_count += 1 if poss_arr_count > 0 else 0
    arrangement_count += poss_arr_count

print(f"Answer 1: { valid_pattern_count }")
print(f"Answer 2: { arrangement_count }")