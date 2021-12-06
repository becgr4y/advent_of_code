import numpy as np


def list_to_binary(my_list):
    return int("".join(list(my_list.astype(str))), 2)


with open("2021/inputs/3") as f:
    data = np.array([list(line.strip()) for line in f]).astype(int)

# Part 1
gamma = np.round(np.sum(data, axis=0) / data.shape[0], 0).astype(int)
epsilon = 1 - gamma

print(f"Part 1: {list_to_binary(gamma) * list_to_binary(epsilon)}")

# Part 2

oxygen_search = np.array(data)
for column_number in range(data.shape[1]):
    percentage_ones = (
        np.sum(oxygen_search[:, column_number])
        / oxygen_search[:, column_number].shape[0]
    )
    if percentage_ones == 0.5:
        most_common = 1
    else:
        most_common = np.round(percentage_ones)
    keep_indices = np.where(oxygen_search[:, column_number] == most_common)
    oxygen_search = oxygen_search[keep_indices]
    if oxygen_search.shape[0] == 1:
        break

C02_search = np.array(data)
for column_number in range(data.shape[1]):
    percentage_ones = (
        np.sum(C02_search[:, column_number]) / C02_search[:, column_number].shape[0]
    )
    if percentage_ones == 0.5:
        least_common = 0
    else:
        least_common = 1 - np.round(percentage_ones)
    keep_indices = np.where(C02_search[:, column_number] == least_common)
    C02_search = C02_search[keep_indices]
    if C02_search.shape[0] == 1:
        break

print(f"Part 2: {list_to_binary(oxygen_search[0]) * list_to_binary(C02_search[0])}")
