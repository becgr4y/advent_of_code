import numpy as np

with open("2021/inputs/1") as f:
    data = [int(line.strip()) for line in f]


def count_number_of_increases(data):
    data_change = np.subtract(data[1:], data[:-1])
    return np.sum(data_change > 0)


# Part 1
print(f"Part 1: Measurement increased {count_number_of_increases(data)} times")

# Part 2
sliding_window = np.convolve(np.array(data), np.ones(3), mode="valid")
print(
    f"Part 2: Measurement increased {count_number_of_increases(sliding_window)} times"
)
