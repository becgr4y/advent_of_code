import numpy as np
import math

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

mean = np.mean(data)
mean_ceil = math.ceil(mean)
mean_floor = math.floor(mean)

sum_ceil = 0
sum_floor = 0


def triangle(number):
    return number * (number + 1) / 2


for item in data:
    sum_ceil += triangle(abs(mean_ceil - item))
    sum_floor += triangle(abs(mean_floor - item))

print(min(sum_ceil, sum_floor))
