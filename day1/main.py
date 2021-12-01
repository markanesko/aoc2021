import time
import os

cwd = os.getcwd()

input_path = os.path.join(cwd, 'input.txt')


def count_increasing(lines=[]):

    count = 0

    for index, element in enumerate(lines):
        if index == 0:
            continue

        if element >= lines[index - 1]:
            count += 1
            continue

    print(f'number of times depth increased is {count}')

    return count


def three_measurement(lines=[]):

    count = 0
    step = 3

    for index in range(0, len(lines) - 2, 1):
        next = sum(lines[index + 1: index + step + 1])
        current = sum(lines[index: index + 3])

        if next > current:
            count += 1

    print(f'number of three-measurement increases is {count}')

    return count


def run():

    lines = []

    with open(input_path) as file:
        lines = file.readlines()
        lines = [int(line.rstrip()) for line in lines]

    _ = count_increasing(lines)

    _ = three_measurement(lines)

    return 0


def main():

    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
