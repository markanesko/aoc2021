import time
import os

cwd = os.getcwd()
input_path = os.path.join(cwd, 'input.txt')

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137,
}

points_auto_complete = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4,

}

opening_closing = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<',
}

def read_input():
    lines = []

    with open(input_path) as file:
        data = file.readlines()
        lines = [el.rsplit()[0] for el in data]

    return lines

def get_scores(line):

    opening_stack = []

    for i in range(0, len(line)):
        if line[i] in opening:
            opening_stack.append(line[i])
            
        if line[i] in closing:
            opening_pair = opening_closing[line[i]]
            last_opening = opening_stack.pop()

            if opening_pair != last_opening:
                return points[line[i]], True
    
    auto_close_score = 0

    while opening_stack != []:
        poped_element = opening_stack.pop()
        auto_close_score = auto_close_score * 5 + points_auto_complete[poped_element]
            
    return auto_close_score, False


def run():

    lines = read_input()

    score = 0
    auto_complete_scores = []

    for line in lines:
        point, corrupted = get_scores(line)
        
        if corrupted:
            score += point
            continue
        
        auto_complete_scores.append(point)

    print(f'final score on corrupted => {score}')

    auto_complete_scores = sorted(auto_complete_scores)
    print(f'median = {auto_complete_scores[int(len(auto_complete_scores) / 2)]}')

    return 0


def main():
    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
