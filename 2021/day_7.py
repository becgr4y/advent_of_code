import numpy as np

with open("2021/inputs/7") as f:
    data = np.array([int(item) for line in f for item in line.strip().split(",")])

# Part 1

median = np.round(np.median(data))

sum = 0

for item in data:
    sum += abs(median - item)

print(median)
print(sum)

# Part 2

for item in data:
    distance = item
    cost = distance * (distance + 1) / 2
    sum += cost
best = sum

for position in range(1, np.max(data) + 1):
    sum = 0
    for item in data:
        distance = abs(position - item)
        cost = distance * (distance + 1) / 2
        sum += cost
    if sum < best:
        best = sum
        best_position = position

print(best_position)
print(best)

# Part 2 w/ maths

X = np.sum(data)
N = len(data)

print(0.5 * (2 * X - N) / N)
