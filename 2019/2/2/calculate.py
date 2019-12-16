# https://adventofcode.com/2019/day/2

import copy
import os


def read_values():
    with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
        for line in f:
            return list(map(int, line.strip().split(",")))


def intcode_computer(values, key1=12, key2=2):
    # Set Error State
    values[1] = key1
    values[2] = key2

    index = 0
    while True:
        if index >= len(values) - 1:
            break

        current_value = values[index]

        if current_value == 99:
            break
        elif current_value == 1:
            values[values[index + 3]] = (
                values[values[index + 1]] + values[values[index + 2]]
            )
        elif current_value == 2:
            values[values[index + 3]] = (
                values[values[index + 1]] * values[values[index + 2]]
            )

        index += 4

    return values[0]


source_values = read_values()
for i in range(0, 100):
    for x in range(0, 100):
        if intcode_computer(copy.deepcopy(source_values), i, x) == 19690720:
            print(f"i: {i} x: {x} :: {100 * i + x}")
