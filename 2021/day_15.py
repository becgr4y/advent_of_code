import numpy as np

with open("2021/inputs/15") as f:
    data = np.array([[int(digit) for digit in line.strip()] for line in f])

width = data.shape[0]
height = data.shape[1]

node_labels = {str(x) + "-" + str(y): None for x in range(width) for y in range(height)}

node_distances = {}
for key, val in node_labels.items():
    x = int(key.split("-")[0])
    y = int(key.split("-")[1])
    neighbours = {}
    for coords in [[x - 1, y], [x, y + 1], [x + 1, y], [x, y - 1]]:
        if (
            coords[0] >= 0
            and coords[0] < width
            and coords[1] >= 0
            and coords[1] < height
        ):
            neighbours[str(coords[0]) + "-" + str(coords[1])] = data[
                coords[0], coords[1]
            ]
    node_distances[key] = neighbours

unvisited = node_labels
visited = {}
current = "0-0"
current_distance = 0
unvisited[current] = current_distance

# Part 1

while True:
    for neighbour, distance in node_distances[current].items():
        if neighbour not in unvisited:
            continue
        new_distance = current_distance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
            unvisited[neighbour] = new_distance
    visited[current] = current_distance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[f"{height-1}-{width-1}"])

# Part 2

bigger = np.zeros((width * 5, height * 5))

for row in range(height * 5):
    for col in range(width * 5):
        original_cell = data[row % height, col % width]
        offset = row // height + col // width
        value = (original_cell + (offset - 1)) % 9 + 1
        bigger[row, col] = value

width = bigger.shape[0]
height = bigger.shape[1]

node_labels = {str(x) + "-" + str(y): None for x in range(width) for y in range(height)}

node_distances = {}
for key, val in node_labels.items():
    x = int(key.split("-")[0])
    y = int(key.split("-")[1])
    neighbours = {}
    for coords in [[x - 1, y], [x, y + 1], [x + 1, y], [x, y - 1]]:
        if (
            coords[0] >= 0
            and coords[0] < width
            and coords[1] >= 0
            and coords[1] < height
        ):
            neighbours[str(coords[0]) + "-" + str(coords[1])] = bigger[
                coords[0], coords[1]
            ]
    node_distances[key] = neighbours

unvisited = node_labels
visited = {}
current = "0-0"
current_distance = 0
unvisited[current] = current_distance

while True:
    if len(unvisited) % 1000 == 0:
        print(len(unvisited))
    for neighbour, distance in node_distances[current].items():
        if neighbour not in unvisited:
            continue
        new_distance = current_distance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > new_distance:
            unvisited[neighbour] = new_distance
    visited[current] = current_distance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items()]
    current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

print(visited[f"{height-1}-{width-1}"])
