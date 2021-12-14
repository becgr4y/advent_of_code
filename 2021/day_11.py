import numpy as np

with open("2021/inputs/11") as f:
    data = np.array([[int(item) for item in line.strip()] for line in f])

total_flashes = 0

width = data.shape[0]
height = data.shape[1]

# Part 1

part_1 = data

for i in range(100):
    flashed = []
    part_1 = part_1 + np.ones((part_1.shape))
    greater_than_nine = np.where(part_1 > 9)
    flashing = [[x, y] for x, y in zip(greater_than_nine[0], greater_than_nine[1])]
    while flashing:
        flash_coords = flashing.pop()
        part_1[flash_coords[0], flash_coords[1]] = 0
        total_flashes += 1
        flashed.append(flash_coords)
        x = flash_coords[0]
        y = flash_coords[1]
        adjacent_coords = [
            [x - 1, y],
            [x - 1, y + 1],
            [x, y + 1],
            [x + 1, y + 1],
            [x + 1, y],
            [x + 1, y - 1],
            [x, y - 1],
            [x - 1, y - 1],
        ]
        for coords in adjacent_coords:
            if (
                coords[0] >= 0
                and coords[0] < width
                and coords[1] >= 0
                and coords[1] < height
                and coords not in flashed
                and coords not in flashing
            ):
                part_1[coords[0], coords[1]] += 1
                if part_1[coords[0], coords[1]] > 9:
                    flashing.append(coords)

print(total_flashes)

# Part 2

part_2 = data

for i in range(1000):
    flashed = []
    part_2 = part_2 + np.ones((part_2.shape))
    greater_than_nine = np.where(part_2 > 9)
    flashing = [[x, y] for x, y in zip(greater_than_nine[0], greater_than_nine[1])]
    while flashing:
        flash_coords = flashing.pop()
        part_2[flash_coords[0], flash_coords[1]] = 0
        flashed.append(flash_coords)
        x = flash_coords[0]
        y = flash_coords[1]
        adjacent_coords = [
            [x - 1, y],
            [x - 1, y + 1],
            [x, y + 1],
            [x + 1, y + 1],
            [x + 1, y],
            [x + 1, y - 1],
            [x, y - 1],
            [x - 1, y - 1],
        ]
        for coords in adjacent_coords:
            if (
                coords[0] >= 0
                and coords[0] < width
                and coords[1] >= 0
                and coords[1] < height
                and coords not in flashed
                and coords not in flashing
            ):
                part_2[coords[0], coords[1]] += 1
                if part_2[coords[0], coords[1]] > 9:
                    flashing.append(coords)
    if len(flashed) == width * height:
        print(i + 1)
        break
