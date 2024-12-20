file = open("./Inputs/day1.txt", "r")
left = []
right = []
for line in file:
    a = line.split()
    left.append(int(a[0]))
    right.append(int(a[1]))

file.close()

left.sort()
right.sort()

dist = []
sim = []
for i in range(0, len(left)):
    dist.append(abs(left[i] - right[i]))
    sim.append(left[i] * right.count(left[i]))

print(f"Answer 1: {sum(dist)}")
print(f"Answer 2: {sum(sim)}")

