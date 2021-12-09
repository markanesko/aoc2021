import time
import os
import numpy as np

from collections import defaultdict

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')

one_len = 2
four_len = 4
seven_len = 3
eight_len = 7


def read_input():
    sequence = []

    with open(input_path) as file:
        data = file.readlines()

        sequence = [line.replace('\n', '').split(' | ') for line in data]

    return sequence


def decode_signals(signals):
    signal_map = defaultdict(list)

    for el in signals.split(' '):
        signal_map[len(el)].append(el)

    one = set(list(signal_map[one_len][0]))
    four = set(list(signal_map[four_len][0]))
    seven = set(list(signal_map[seven_len][0]))
    eight = set(list(signal_map[eight_len][0]))
    six = None
    three = None
    two = None
    five = None
    nine = None
    zero = None

    for el in signal_map[6]:
        six = set(list(el))
        if len(one.intersection(six)) == 1:
            break

    for el in signal_map[5]:
        three = set(list(el))
        if len(one.intersection(three)) == 2:
            break

    for el in signal_map[5]:
        checker = set(list(el))
        if len(six.intersection(checker)) == 5:
            five = checker
            break

    nine_sum = five.union(one)

    for el in signal_map[6]:
        nine = set(list(el))
        if len(nine_sum.intersection(nine)) == 6:
            break

    for el in signal_map[6]:
        zero = set(list(el))
        if zero != six and zero != nine:
            break

    for el in signal_map[5]:
        checker = set(list(el))
        if checker != three and checker != five:
            two = checker

    # print(f' 1 = {one}\t 2 = {two}\t 3 = {three}\t 4 = {four}\t 5 = {five}\t 6 = {six}\t 7 = {seven}\t 8 = {eight}\t 9 = {nine}\n')

    decoded_numbers = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
    }

    return decoded_numbers


def calcualte_number(numbers, outputs):

    list_outputs = outputs.split(' ')

    final = 0

    for el in list_outputs:
        el_set = set(list(el))
        for k, v in numbers.items():
            if len(el_set) == len(v) and len(v.difference(el_set)) == 0:
                final = final * 10 + k

    return final


def run():
    sequence = read_input()
    np_sequence = np.array(sequence)

    outputs = np_sequence[:, 1]

    counter = 0
    for el in outputs:
        for d in el.split(' '):
            if len(d) == 2 or len(d) == 3 or len(d) == 4 or len(d) == 7:
                counter += 1

    print(f'number of ocurances {counter}')

    final = 0

    for pair in sequence:
        decoded = decode_signals(pair[0])
        result = calcualte_number(decoded, pair[1])

        final += result

    print(f'final sum is {final}')

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
