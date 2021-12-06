import time
import os
import numpy as np


cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')

def read_input():

    lanternfish = []

    with open(input_path) as file:
        data = file.readlines()
        lanternfish = data[0].split(',')
        lanternfish = [ int(fish) for fish in lanternfish]

    return lanternfish

def run():

    lanternfish = read_input()
    np_lanternfish = np.array(lanternfish)
    n_days = 256

    # for day in range(n_days):
        
        # num_new_fishes = 0
        # for index, ttr in enumerate(lanternfish):
        #     if ttr == 0:
        #         lanternfish[index] = 6
        #         num_new_fishes += 1
        #         continue
        #     lanternfish[index] = lanternfish[index] - 1
        
        # for i in range(num_new_fishes):
        #     lanternfish.append(8)

    # print(len(lanternfish))

    for day in range(n_days):
        print(f'day => {day}')

        reproduced_array = (np_lanternfish == 0)
        no_reproduce_array = (np_lanternfish != 0)

        num_of_zeros = reproduced_array.sum()

        reproduced_array = reproduced_array * 6
        no_reproduce_array = no_reproduce_array * (-1)

        result_array = reproduced_array + no_reproduce_array
        np_lanternfish += result_array

        for i in range(num_of_zeros):
            np_lanternfish = np.append(np_lanternfish, 8)


    print(len(np_lanternfish))


    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
