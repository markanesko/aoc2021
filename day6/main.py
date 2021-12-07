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

def init_population_dict(lanternfish):
    population = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }
    
    for fish in lanternfish:
        population[fish] = population[fish] + 1
            

    return population

def run():

    lanternfish = read_input()
    n_days = 256

    population = init_population_dict(lanternfish)

    for day in range(n_days):

        temp_population = {
            0: population[1],
            1: population[2],
            2: population[3],
            3: population[4],
            4: population[5],
            5: population[6],
            6: population[7] + population[0],
            7: population[8],
            8: population[0],
        }
        population = temp_population
    
    print(f'population is {population}')

    population_size = sum(list(population.values()))

    print(f'population size is {population_size}')

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
