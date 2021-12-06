from types import new_class
import numpy as np

with open("2021/inputs/6") as f:
    data = [int(item) for line in f for item in line.strip().split(",")]

fish = np.array(data)

# Part 1

for day in range(80):
    fish = fish - np.ones((len(fish)))
    ready_for_babies = np.where(fish == -1)
    fish[ready_for_babies] = 6
    new_fish = 8 * np.ones((len(ready_for_babies[0])))
    fish = np.concatenate((fish, new_fish), axis=0)

print(len(fish))

# Part 2

bucketed_fish = [data.count(number) for number in range(9)]

for day in range(256):
    ready_to_spawn = bucketed_fish[0]
    for bucket in [0, 1, 2, 3, 4, 5, 6, 7]:
        bucketed_fish[bucket] = bucketed_fish[bucket + 1]
    bucketed_fish[6] += ready_to_spawn
    bucketed_fish[8] = ready_to_spawn

print(sum(bucketed_fish))
