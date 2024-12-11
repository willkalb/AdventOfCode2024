from functools import reduce

def buildUpdateRules(update):
    rules = []
    for i in range(0, len(update)):
        for j in range(0, len(update)):
            if i == j:
                continue

            if i > j:
                rules.append([update[j], update[i]])
                continue

            rules.append([update[i], update[j]])

    return list(map(list, list(set(map(tuple, rules)))))

def getBefore(rules, list, page, totalChildCount = 0):
    children = [ (r[0], getBefore(rules, list, r[0], totalChildCount := totalChildCount + 1)) for r in rules if r[1] == page and r[0] in list and r[1] in list ]
    return (children, totalChildCount)

rules = []
updates = []
with open("./Inputs/day5.txt", "r") as f:
    for line in f:
        clean_line = line.strip()
        if clean_line == "":
            continue

        if clean_line.find("|") >= 0:
            rules.append(list(map(int, clean_line.split("|"))))
            continue

        updates.append(list(map(int, clean_line.split(","))))

correct_updates = []
incorrect_updates = []
for update in updates:
    rules_to_check = buildUpdateRules(update)
    if reduce(lambda a, b: a and b, [r in rules for r in rules_to_check]):
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)

mid_sum = 0
for ic in incorrect_updates:
    for p in ic:
        pivot = p
        update = ic
        before = getBefore(rules, update, pivot)

        if before[1] == int(len(ic)/2):
            mid_sum = mid_sum + p
            break

print(f"Answer 1: { sum([ u[int(len(u)/2)] for u in correct_updates ]) }")
print(f"Answer 2: { mid_sum }")