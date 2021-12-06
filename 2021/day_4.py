import numpy as np

with open("2021/inputs/4") as f:
    data = [line for line in f]

called_numbers = list(map(int, data[0].replace("\n", "").split(",")))
lines_between_boards = [index for index, value in enumerate(data) if value == "\n"]
list_of_boards = []

for line in lines_between_boards:
    board = np.array(
        [
            [int(item) for item in row.replace("\n", "").split(" ") if item != ""]
            for row in data[line + 1 : line + 6]
        ]
    )
    list_of_boards.append(board)

# Part 1
board_number = None
list_of_checkers = [np.zeros((5, 5)) for board in list_of_boards]

for number in called_numbers:
    for board_index in range(len(list_of_boards)):
        indices = np.where(list_of_boards[board_index][0:5, 0:5] == number)
        list_of_checkers[board_index][indices] = 1
        if (5 in np.sum(list_of_checkers[board_index], axis=0)) | (
            5 in np.sum(list_of_checkers[board_index], axis=1)
        ):
            board_number = board_index
            break
    if board_number is not None:
        break

print(
    int(
        np.sum((1 - list_of_checkers[board_number]) * list_of_boards[board_number])
        * number
    )
)

# Part 2
list_of_checkers = [np.zeros((5, 5)) for board in list_of_boards]
board_number = None
total_number_of_boards = len(list_of_boards)
completed_boards = np.zeros((total_number_of_boards))

for number in called_numbers:
    for board_index in range(len(list_of_boards)):
        indices = np.where(list_of_boards[board_index][0:5, 0:5] == number)
        list_of_checkers[board_index][indices] = 1
        if (5 in np.sum(list_of_checkers[board_index], axis=0)) | (
            5 in np.sum(list_of_checkers[board_index], axis=1)
        ):
            completed_boards[board_index] = 1
        if int(np.sum(completed_boards)) == total_number_of_boards:
            board_number = board_index
            break
    if board_number is not None:
        break

print(
    int(
        np.sum((1 - list_of_checkers[board_number]) * list_of_boards[board_number])
        * number
    )
)
