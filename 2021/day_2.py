import numpy as np

with open("2021/inputs/2") as f:
    data = [line.strip().split(" ") for line in f]

# Part 1
print("---Part 1---")

horizontal = 0
depth = 0

for instruction in data:
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
    elif instruction[0] == "up":
        depth -= int(instruction[1])
    else:
        depth += int(instruction[1])

print(f"Depth: {depth}")
print(f"Horizontal: {horizontal}")
print(f"Product: {depth * horizontal}")

# Part 2
print("---Part 2---")

horizontal = 0
depth = 0
aim = 0

for instruction in data:
    if instruction[0] == "forward":
        horizontal += int(instruction[1])
        depth += int(instruction[1]) * aim
    elif instruction[0] == "up":
        aim -= int(instruction[1])
    else:
        aim += int(instruction[1])

print(f"Depth: {depth}")
print(f"Horizontal: {horizontal}")
print(f"Product: {depth * horizontal}")
