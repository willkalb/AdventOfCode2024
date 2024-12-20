from functools import reduce

robots = []

with open("./Inputs/day14.txt", "r") as f:
    for line in f.read().split("\n"):
        robot_prop_dict = dict()
        props = line.split(" ")
        for prop in props:
            key = prop[0]
            start = prop.find("=") + 1
            mid = prop.find(",")

            robot_prop_dict[key] = (int(prop[start:mid]), int(prop[mid + 1:]))
        
        robots.append(robot_prop_dict)

map_size = (101, 103)

def printMap(points):
    for y in range(map_size[1]):
        row = ""
        for x in range(map_size[0]):
            if (x, y) in points:
                row += "."
            else:
                row += " "
        print(row)

def getQuadrant(getQuadrant_point):
    if getQuadrant_point[0] < map_size[0] // 2 and getQuadrant_point[1] < map_size[1] // 2:
        return 0
    if getQuadrant_point[0] > map_size[0] // 2 and getQuadrant_point[1] < map_size[1] // 2:
        return 1
    if getQuadrant_point[0] < map_size[0] // 2 and getQuadrant_point[1] > map_size[1] // 2:
        return 2
    if getQuadrant_point[0] > map_size[0] // 2 and getQuadrant_point[1] > map_size[1] // 2:
        return 3

iterations = 100
quadrants = [0, 0, 0, 0]
for robot in robots:
    final_p = ((robot["p"][0] + (robot["v"][0] * iterations)) % map_size[0], (robot["p"][1] + (robot["v"][1] * iterations)) % map_size[1])
    robot["np"] = final_p
    quad_i = getQuadrant(final_p)
    if quad_i == None:
        continue
    quadrants[quad_i] += 1

safety_factor = float("inf")
safety_points = []
safety_quadrants = [0, 0, 0, 0]
safety_seconds = 0
for i in range(6750):
    points = []
    safety_quadrants = [0, 0, 0, 0]
    for robot in robots:
        point = ((robot["p"][0] + (robot["v"][0] * i)) % map_size[0], (robot["p"][1] + (robot["v"][1] * i)) % map_size[1])
        points.append(point)

        quad_i = getQuadrant(point)
        if quad_i == None:
            continue
        safety_quadrants[quad_i] += 1
    
    if (new_safety_factor := reduce(lambda a, c: a * c, safety_quadrants)) < safety_factor:
        safety_factor = new_safety_factor
        safety_points = points
        safety_seconds = i

printMap(safety_points)

print(f"Answer 1: { reduce(lambda a, c: a * c, quadrants) }")
print(f"Answer 2: { safety_seconds }")