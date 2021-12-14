import numpy as np

with open("2021/inputs/10") as f:
    data = [[item for item in line.strip()] for line in f]

corrupt_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

incomplete_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

open_close_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

points_sum = 0
scores = []

for row in data:
    used_characters = []
    score = 0
    for character in row:
        if character in open_close_map.values():
            if character == open_close_map[used_characters[-1]]:
                used_characters.pop()
            else:
                points_sum += corrupt_points[character]
                used_characters = []
                break
        else:
            used_characters.append(character)
    if used_characters:
        for character in [open_close_map[x] for x in used_characters[::-1]]:
            score = (score * 5) + incomplete_points[character]
        scores.append(score)

print(points_sum)
print(sorted(scores)[int((len(scores) - 1) / 2)])
