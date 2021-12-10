import time
import os

from operator import mul
from functools import reduce

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')


def read_input():
    heightmap = []

    with open(input_path) as file:
        data = file.readlines()
        data = [ el.rsplit()[0] for el in data]

        heightmap = data


    return heightmap

def check_min(arr = [], el = 0):
    result = True

    for check in arr:
        if check <= el:
            result = False 

    # if el in arr:
    #     result = False

    return result

def run_first_part():
    heightmap = read_input()
    row_len = len(heightmap[0])

    risk_level_sum = 0

    low_points = []

    for row_index, row in enumerate(heightmap):
        # print(f'row[row_index][3] = {row[3]}')

        if row_index == 0:
            bottom = int(heightmap[row_index + 1][0])
            right = int(heightmap[row_index][0 + 1])
            element = int(heightmap[row_index][0])

            min_element = check_min([bottom, right], element)

            if min_element:
                low_points.append((row_index, 0))
                risk_level_sum += element + 1

            element = int(heightmap[row_index][row_len - 1])
            left = int(heightmap[row_index][row_len - 1 - 1])
            bottom = int(heightmap[row_index + 1][row_len - 1])

            min_element = check_min([bottom, left], element)

            if min_element:
                low_points.append((row_index, row_len - 1))
                risk_level_sum += element + 1

            for i in range(1, row_len - 1):
                element = int(heightmap[row_index][i])
                right = int(heightmap[row_index][i + 1])
                left = int(heightmap[row_index][i - 1])
                bottom = int(heightmap[row_index + 1][i])

                min_element = check_min([bottom, right, left], element)

                if min_element:
                    low_points.append((row_index, i))
                    risk_level_sum += element + 1

            continue

        if row_index == len(heightmap) - 1:
            element = int(heightmap[row_index][0])
            right = int(heightmap[row_index][0 + 1])
            top = int(heightmap[row_index - 1][0])

            min_element = check_min([top, right], element)

            if min_element:
                low_points.append((row_index, 0))
                risk_level_sum += element + 1

            element = int(heightmap[row_index][row_len - 1])
            left = int(heightmap[row_index][row_len - 1 - 1])
            top = int(heightmap[row_index - 1][row_len - 1])

            min_element = check_min([top, left], element)

            if min_element:
                low_points.append((row_index, row_len - 1))
                risk_level_sum += element + 1

            for i in range(1, row_len - 1):
                element = int(heightmap[row_index][i])
                right = int(heightmap[row_index][i + 1])
                left = int(heightmap[row_index][i - 1])
                top = int(heightmap[row_index -1][i])

                min_element = check_min([top, right, left], element)

                if min_element:
                    low_points.append((row_index, i))
                    risk_level_sum += element + 1

            continue

        element = int(heightmap[row_index][0])
        bottom = int(heightmap[row_index + 1][0])
        right = int(heightmap[row_index][0 + 1])
        top = int(heightmap[row_index - 1][0])

        min_element = check_min([top, bottom, right], element)

        if min_element:
            low_points.append((row_index, 0))
            risk_level_sum += element + 1
        
        element = int(heightmap[row_index][row_len - 1])
        left = int(heightmap[row_index][row_len - 1 - 1])
        top = int(heightmap[row_index - 1][row_len - 1])
        bottom = int(heightmap[row_index + 1][row_len - 1])

        min_element = check_min([top, bottom, left], element)

        if min_element:
            low_points.append((row_index, row_len - 1))
            risk_level_sum += element + 1

        for i in range(1, row_len - 1):
            element = int(heightmap[row_index][i])
            right = int(heightmap[row_index][i + 1])
            left = int(heightmap[row_index][i - 1])
            top = int(heightmap[row_index -1][i])
            bottom = int(heightmap[row_index + 1][i])

            min_element = check_min([top, right, left, bottom], element)

            if min_element:
                low_points.append((row_index, i))
                risk_level_sum += element + 1

    print(f'risk_level_sum = {risk_level_sum}')

    return low_points


def find_basin_2(root, basinmap, basinheight, basinwidth, area, checked = []):

    if root in checked:
        return area

    temp_checked = checked
    temp_checked.append(root)

    x, y = root[0], root[1]

    left = (x, y - 1)
    
    right = (x, y + 1)
    
    down = (x + 1, y)

    up = (x - 1, y)

    temp_area = area
    
    if y != 0 and left not in checked:
        if basinmap[x][y - 1] != '*':
            temp_area += 1
            temp_area = find_basin_2(left, basinmap, basinheight, basinwidth, temp_area, temp_checked)
    
    if y != basinwidth - 1 and right not in checked:
        if basinmap[x][y + 1] != '*':
            temp_area += 1
            temp_area = find_basin_2(right, basinmap, basinheight, basinwidth, temp_area, temp_checked)

    if (x != basinheight - 1) and down not in checked:
        if basinmap[x + 1][y] != '*':
            temp_area += 1
            temp_area = find_basin_2(down, basinmap, basinheight, basinwidth, temp_area, temp_checked)

    if x != 0 and up not in checked:
        if basinmap[x - 1][y] != '*':
            temp_area += 1
            temp_area = find_basin_2(up, basinmap, basinheight, basinwidth, temp_area, temp_checked)

    return temp_area


def run_second_part(low_points):

    heightmap = read_input()
    basinmap = []
    row_len = len(heightmap[0])
    
    for row in heightmap:
        row_string = ''

        for i in range(0, row_len):
            if row[i] != '9':
                row_string += row[i]
                continue

            row_string += '*'
        basinmap.append(row_string)

    save_file = os.path.join(cwd, 'output.txt')
    
    with open(save_file, 'w') as file:
        file.write('\n'.join(basinmap))

    basin_areas = []

    for low in low_points:
        area = find_basin_2(low, basinmap, len(heightmap), row_len, 0)
        basin_areas.append(area + 1)

    basin_areas = sorted(basin_areas, reverse=True)
    basin_areas = basin_areas[:3]

    print(f'basin_areas = {basin_areas}')

    result = reduce(mul, basin_areas, 1)

    print(f'product is {result}')


    

    return

def run():

    low_points = run_first_part()

    run_second_part(low_points)

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
