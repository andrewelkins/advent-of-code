# https://adventofcode.com/2019/day/2

import os

values = []
with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
    for line in f:
        values = list(map(int, line.strip().split(",")))


index = 0
while True:
    if index >= len(values) - 1:
        break

    mode_string = str(f"{values[index]:06}")

    param1 = 0
    param2 = 0
    param3 = 0

    try:
        param1 = values[index + 1] if int(mode_string[-3]) == 0 else index + 1
        param2 = values[index + 2] if int(mode_string[-4]) == 0 else index + 2
        param3 = values[index + 3] if int(mode_string[-5]) == 0 else index + 3
    except IndexError:
        pass

    current_value = int(mode_string[-2:])
    index_increment = 4

    if current_value == 99:
        break
    elif current_value == 1:
        values[param3] = values[param1] + values[param2]
    elif current_value == 2:
        values[param3] = values[param1] * values[param2]
    elif current_value == 3:
        values[param1] = int(input("Enter value: "))
        index_increment = 2
    elif current_value == 4:
        print(values[param1])
        index_increment = 2

    index += index_increment
