import numpy as np

with open("2021/inputs/13") as f:
    data = [line.strip() for line in f]

instructions_split = data.index("")
coords = [
    [int(coord) for coord in item.split(",")] for item in data[:instructions_split]
]

instructions = data[instructions_split + 1 :]

width = max([row[0] for row in coords])
height = max([row[1] for row in coords])

paper = np.zeros((width + 1, height + 2))

instructions = [row.split("fold along ")[1].split("=") for row in instructions]

for row in coords:
    paper[row[0], row[1]] = 1

# Parts 1 & 2

first = True

for row in instructions:
    if row[0] == "x":
        under = paper[: int(row[1]), :]
        over = paper[int(row[1]) + 1 :, :]
        over = np.flipud(over)
        paper = np.add(under, over)
        paper = np.minimum(paper, np.ones(paper.shape))
    else:
        under = paper[:, : int(row[1])]
        over = paper[:, int(row[1]) + 1 :]
        over = np.fliplr(over)
        paper = np.add(under, over)
        paper = np.minimum(paper, np.ones(paper.shape))
    if first:
        print(np.sum(paper))
        first = False

print(np.swapaxes(paper, 0, 1))
