import time
import os
import numpy as np

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')

def read_input():
    crabs = []

    with open(input_path) as file:
        data = file.readlines()[0]
        crabs = [int(crab) for crab in data.split(',')]

    return crabs

def sum_num(n):
    value = 0
    for i in range(1, n + 1):
        value += i
    
    return value


def run():

    crabs = read_input()

    min_value = min(crabs)
    max_value = max(crabs)

    align = dict.fromkeys(range(min_value, max_value + 1), 0)

    counter = lambda x: int(x * (x + 1) / 2)
    vfunc = np.vectorize(counter)

    for position in range(min_value, max_value + 1):
        # print(f'initial np_crabs = {np_crabs}')
        np_crabs = np.array(crabs)
        np_crabs = abs(np_crabs - position)
        np_crabs = vfunc(np_crabs)
        cost = np.sum(np_crabs)
        align[position] = cost
        # print(f'modified np_crabs = {np_crabs}')
    
    min_cost = min(list(align.values()))
    print(f'minimal cost is {min_cost}')

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
