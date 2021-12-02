import time
import os

cwd = os.getcwd()
input_file = os.path.join(cwd, 'input.txt')


def parse_command(command):

    parsed = [
        command[0],
        int(command[1]),
    ]

    return parsed


def create_commands():

    commands = []

    with open(input_file) as file:
        commands = file.readlines()
        commands = [parse_command(command.rstrip().split(' '))
                    for command in commands]

    return commands


def run_no_aim(commands=[]):

    horizontal = 0
    depth = 0

    for command in commands:
        instruction = command[0]
        value = command[1]

        if 'forward' == instruction:
            horizontal += value
            continue
        if 'down' == instruction:
            depth += value
            continue
        depth -= value

    print(f'final position (h, d) = ({horizontal}, {depth})')
    print(f'final product is {horizontal * depth}')

    return horizontal * depth


def run_with_aim(commands=[]):

    horizontal = 0
    aim = 0
    depth = 0

    for command in commands:
        instruction = command[0]
        value = command[1]

        if 'forward' == instruction:
            horizontal += value
            depth += aim * value
            continue

        if 'down' == instruction:
            aim += value
            continue

        aim -= value

    print(f'final position (h, d) = ({horizontal}, {depth})')
    print(f'final product is {horizontal * depth}')

    return horizontal * depth


def run():

    commands = create_commands()

    _ = run_no_aim(commands)

    _ = run_with_aim(commands)

    return 0


def main():

    start_time = time.time()

    rc = run()

    print(f'finished in {time.time() - start_time}')

    return rc


if __name__ == '__main__':
    main()
