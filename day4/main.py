import time
import os
import numpy as np

from itertools import zip_longest

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')


def grouper(iterable, n, fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def make_tuples(input_row):

    tupled_list = [(int(el), False) for el in input_row]

    return tupled_list


def read_input():

    number_draw = []
    boards = []

    with open(input_path) as file:
        data = file.readlines()
        number_draw = data[0].rsplit()[0].split(',')
        number_draw = [int(num) for num in number_draw]

        data = data[1:]

        data = [make_tuples(row.rsplit()) for row in data if row not in ['\n']]

        N = 5
        boards = np.array([data[n:n+N] for n in range(0, len(data), N)])

    return number_draw, boards


def mark_board(board, number, marked_numbers):

    if number in marked_numbers:
        return board, False

    changed = False
    temp_board = board
    for index, row in enumerate(board):
        if (number, False) in row:
            for row_index, row_element in enumerate(row):
                if row_element[0] == number:
                    temp_board[index][row_index] = (number, True)
                    changed = True

    return temp_board, changed


def evaluate_board(board):

    x = np.array(board)

    for i in range(5):
        numpy_row = x[i, :]
        numpy_column = x[:, i]

        numpy_row_marked = (numpy_row[:, 1] == 1).sum()
        numpy_column_marked = (numpy_column[:, 1] == 1).sum()

        if numpy_row_marked == 5:
            return True

        if numpy_column_marked == 5:
            return True

    return False


def calculate_unmarked(board):
    unmarked_sum = 0

    for row in board:
        for el in row:
            if el[1] == 0:
                unmarked_sum += el[0]

    return unmarked_sum


def run():

    number_draw, boards = read_input()
    marked_numbers = []
    boards = boards
    winners = []
    winners_values = []

    for number in number_draw:
        number_changed = False
        for i, b in enumerate(boards):
            if i in winners:
                continue
            board, changed = mark_board(b, number, marked_numbers)

            if not changed:
                continue

            number_changed = True

            boards[i] = board

            winner = evaluate_board(board)

            if winner:
                unmarked_sum = calculate_unmarked(board)
                product = number * unmarked_sum
                winners_values.append(product)
                winners.append(i)

        if number_changed:
            marked_numbers.append(number)

    print(winners_values)

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
