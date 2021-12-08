import numpy as np

with open("2021/inputs/8") as f:
    data = [line.strip() for line in f]

input = [row.split(" | ")[0].split(" ") for row in data]
output = [row.split(" | ")[1].split(" ") for row in data]

# Part 1
output_segment_length = [
    len(inner) for outer in output for inner in outer if len(inner) in [2, 3, 4, 7]
]

print(len(output_segment_length))

# Part 2


def decode_output(current_row, current_output):
    one = [item for item in current_row if len(item) == 2][0]
    seven = [item for item in current_row if len(item) == 3][0]
    four = [item for item in current_row if len(item) == 4][0]
    eight = [item for item in current_row if len(item) == 7][0]

    five_segments = [item for item in current_row if len(item) == 5]
    six_segments = [item for item in current_row if len(item) == 6]

    three = [item for item in five_segments if one[0] in item and one[1] in item][0]

    bottom = [
        letter
        for letter in three
        if letter not in list(seven) and letter not in list(four)
    ][0]
    top_left = [letter for letter in four if letter not in list(three)][0]
    centre = [
        letter for letter in four if letter not in list(seven) and letter != top_left
    ][0]

    zero = [item for item in six_segments if centre not in item][0]

    bottom_left = [
        letter
        for letter in zero
        if letter not in list(seven) and letter != bottom and letter != top_left
    ][0]

    nine = [item for item in six_segments if bottom_left not in item][0]
    six = [item for item in six_segments if item not in [nine, zero]][0]

    five = [
        item for item in five_segments if bottom_left not in item and item != three
    ][0]
    two = [item for item in five_segments if item not in [five, three]][0]

    digit_dict = {
        "".join(sorted(zero)): "0",
        "".join(sorted(one)): "1",
        "".join(sorted(two)): "2",
        "".join(sorted(three)): "3",
        "".join(sorted(four)): "4",
        "".join(sorted(five)): "5",
        "".join(sorted(six)): "6",
        "".join(sorted(seven)): "7",
        "".join(sorted(eight)): "8",
        "".join(sorted(nine)): "9",
    }

    sorted_output = ["".join(sorted(item)) for item in current_output]

    return int("".join([digit_dict[item] for item in sorted_output]))


sum = 0
for i in range(len(input)):
    sum += decode_output(input[i], output[i])

print(sum)
