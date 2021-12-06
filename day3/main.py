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


    for i in range(12):
        column = readings[:, i]
        num_ones = (column == '1').sum()
        num_zeroes = (column == '0').sum()


        if num_ones >= num_zeroes:
            gama_rate += '1'
            epsilon_rate += '0'
            continue
        
        gama_rate += '0'
        epsilon_rate += '1'

    gama_rate = int(gama_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print(f'product of gama and epsilon is {gama_rate * epsilon_rate}')

    oxygen = readings

    for i in range(12):
        
        column = oxygen[:, i]
        num_ones = (column == '1').sum()
        num_zeros = abs(len(column) - num_ones)

        d = '1'

        if num_zeros > num_ones:
            d = '0'

        oxygen = oxygen[column == d, :]

        if len(oxygen) == 1:
            break     
    
    oxygen = ''.join(str(x) for x in oxygen[0])
    oxygen = int(oxygen, 2)
    print(oxygen)

    co2 = readings

    for i in range(12):
        
        column = co2[:, i]
        num_ones = (column == '1').sum()
        num_zeros = abs(len(column) - num_ones)

        d = '0'

        if num_ones < num_zeros:
            d = '1'

        co2 = co2[column == d, :]


        if len(co2) == 1:
            break        

    co2 = ''.join(str(x) for x in co2[0])
    co2 = int(co2, 2)
    print(co2)

    print(f'life supporting rating is {co2 * oxygen}')

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
