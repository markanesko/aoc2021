import time
import os

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')

def parse_vent(vent_input):
    vent_input = ''.join(vent_input)

    vent = vent_input.split('->')
    
    x_coords = [int(x) for x in vent[0].split(',')]
    y_coords = [int(y) for y in vent[1].split(',')]
    
    vent = [x_coords, y_coords]
    
    return vent

def read_input():
    
    vents = []

    with open(input_path) as file:
        data = file.readlines()
        data = [parse_vent(line.rsplit()) for line in data]

        vents = data

    return vents

def parse_horizontal(vents):

    horizontal_vents = []

    for vent in vents:
        x1 = vent[0][0]
        y1 = vent[0][1]
        x2 = vent[1][0]
        y2 = vent[1][1]

        if x1 == x2 or y1 == y2:
            horizontal_vents.append(vent)

    return horizontal_vents



def calculate_points_horizontal(vent):

    points = []

    x1 = vent[0][0]
    y1 = vent[0][1]
    x2 = vent[1][0]
    y2 = vent[1][1]

    if x1 == x2:
        min_y = min(y1, y2)
        max_y = max(y1, y2)

        x = x1

        for y in range(min_y, max_y + 1):
            points.append([x, y])

        return points

    min_x = min(x1, x2)
    max_x = max(x1, x2)

    y = y1

    for x in range(min_x, max_x + 1):
        points.append([x, y])

    return points

def calculate_points_diagonal(vent):
    points = []
    
    x1 = vent[0][0] 
    y1 = vent[0][1]
    x2 = vent[1][0]
    y2 = vent[1][1]

    if y2 == y1:
        return points
    
    if x2 == x1:
        return points

    k = (y2 - y1) / (x2 - x1)

    if abs(k) == 1:
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        for x in range(min_x, max_x + 1):
            y = k * (x - x1) + y1
            points.append([int(x), int(y)])
        
        return points
    
    return points

def run():

    vents = read_input()

    horizontal = parse_horizontal(vents)

    all_points = {}

    for h_vent in horizontal:
        points_on_line = calculate_points_horizontal(h_vent)
        for point in points_on_line:
            point_string = 'k'.join(map(str, point))
            if point_string in all_points:
                all_points[point_string] = all_points[point_string] + 1
                continue
            all_points[point_string] = 1

    danger = [k for k, v in all_points.items() if v > 1]

    print(len(danger))

    for vent in vents:
        diagonal_points = calculate_points_diagonal(vent)
        for point in diagonal_points:
            point_string = 'k'.join(map(str, point))
            if point_string in all_points:
                all_points[point_string] = all_points[point_string] + 1
                continue
            all_points[point_string] = 1

    danger = [k for k, v in all_points.items() if v > 1]

    print(len(danger))


    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
