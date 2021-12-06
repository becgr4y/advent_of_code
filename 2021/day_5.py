import numpy as np

with open("2021/inputs/5") as f:
    data = [list(map(int, line.strip().replace(" -> ", ",").split(","))) for line in f]

num_rows = max([max(row[1], row[3]) for row in data])
num_cols = max([max(row[0], row[2]) for row in data])

vent_map = np.zeros((num_rows + 1, num_cols + 1))

# Part 1

horizontal_vertical_only = [
    row for row in data if (row[0] == row[2]) | (row[1] == row[3])
]

for row in horizontal_vertical_only:
    start_x = min(row[0], row[2])
    start_y = min(row[1], row[3])
    end_x = max(row[0], row[2])
    end_y = max(row[1], row[3])
    if start_x == end_x:
        vent_map[start_y : end_y + 1, start_x] = (
            vent_map[start_y : end_y + 1, start_x] + 1
        )
    else:
        vent_map[start_y, start_x : end_x + 1] = (
            vent_map[start_y, start_x : end_x + 1] + 1
        )

print(len(np.where(vent_map >= 2)[0]))

# Part 2

diagonal = [row for row in data if (row[0] != row[2]) & (row[1] != row[3])]


def get_direction(start, end):
    if end - start > 0:
        return 1
    else:
        return -1


for row in diagonal:
    start_x = row[0]
    start_y = row[1]
    direction_x = get_direction(row[0], row[2])
    direction_y = get_direction(row[1], row[3])
    path_length = abs(row[0] - row[2]) + 1
    for step in range(path_length):
        vent_map[start_y, start_x] = vent_map[start_y, start_x] + 1
        start_x += direction_x
        start_y += direction_y

print(len(np.where(vent_map >= 2)[0]))
