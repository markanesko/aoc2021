import time
import os
import numpy as np

cwd = os.getcwd()
input_file = os.path.join(cwd, 'input.txt')

def split(string):
    return [c for c in string]


def run():

    readings = np.loadtxt(input_file, dtype=str)
    readings = list(readings)
    readings = np.array([split(x) for x in readings])

    gama_rate = ''
    epsilon_rate = ''

    dominant = []

    for i in range(5):
        column = readings[:, i]
        num_ones = (column == '1').sum()
        num_zeroes = (column == '0').sum()

        if num_ones >= num_zeroes:
            gama_rate += '1'
            epsilon_rate += '0'
            dominant.append('1')
            continue
        
        dominant.append('0')
        gama_rate += '0'
        epsilon_rate += '1'

    gama_rate = int(gama_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print(f'product of gama and epsilon is {gama_rate * epsilon_rate}')

    oxygen = []
    co2 = []

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
