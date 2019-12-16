# https://adventofcode.com/2019/day/2

import os

values = []
with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
    for line in f:
        values = list(map(int, line.strip().split(",")))

# Set Error State
values[1] = 12
values[2] = 2

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

print(f"Printing total: {values[0]}")
