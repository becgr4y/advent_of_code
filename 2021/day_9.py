import numpy as np

with open("2021/inputs/9") as f:
    data = np.array([[int(item) for item in line.strip()] for line in f])

width, height = data.shape

# Part 1

result = [
    data[x, y] + 1
    if data[x, y]
    == np.min(
        data[max(0, x - 1) : min(x + 2, width), max(0, y - 1) : min(y + 2, height)]
    )
    else 0
    for x in range(width)
    for y in range(height)
]
print(sum(result))

# Part 2

low_points = [
    (x, y)
    for x in range(width)
    for y in range(height)
    if data[x, y]
    == np.min(
        data[max(0, x - 1) : min(x + 2, width), max(0, y - 1) : min(y + 2, height)]
    )
]


def get_adjacent(point, data):
    width = data.shape[0]
    height = data.shape[1]
    x = point[0]
    y = point[1]
    adjacent_coords = [[x - 1, y], [x, y + 1], [x + 1, y], [x, y - 1]]
    return [
        tuple(coords)
        for coords in adjacent_coords
        if coords[0] >= 0
        and coords[0] < width
        and coords[1] >= 0
        and coords[1] < height
        and data[coords[0], coords[1]] != 9
    ]


basins = []

for low_point in low_points:
    npoints = 0
    points = [low_point]
    while npoints < len(points):
        npoints = len(points)
        for p in points:
            points = list(set(points + get_adjacent(p, data)))
    basins = basins + [len(points)]

print(sorted(basins)[-1] * sorted(basins)[-2] * sorted(basins)[-3])
