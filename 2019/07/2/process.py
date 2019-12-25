# https://adventofcode.com/2019/day/7

from copy import deepcopy
import os
import itertools

values = []
with open(os.path.join(os.path.dirname(__file__), "../../07/data.txt"), "r") as f:
    for line in f:
        values = list(map(int, line.strip().split(",")))


def process(vals):
    index = 0
    result = 0
    values_machine = deepcopy(values)
    while True:
        if index >= len(values_machine) - 1:
            break

        mode_string = str(f"{values_machine[index]:06}")

        param1 = 0
        param2 = 0
        param3 = 0

        try:
            param1 = (
                values_machine[index + 1] if int(mode_string[-3]) == 0 else index + 1
            )
            param2 = (
                values_machine[index + 2] if int(mode_string[-4]) == 0 else index + 2
            )
            param3 = (
                values_machine[index + 3] if int(mode_string[-5]) == 0 else index + 3
            )
        except IndexError:
            pass

        current_value = int(mode_string[-2:])
        index_increment = 4

        if current_value == 99:
            return result
        elif current_value == 1:
            values_machine[param3] = values_machine[param1] + values_machine[param2]
        elif current_value == 2:
            values_machine[param3] = values_machine[param1] * values_machine[param2]
        elif current_value == 3:
            values_machine[param1] = vals.pop(0)
            # values_machine[param1] = val
            index_increment = 2
        elif current_value == 4:
            # print(values_machine[param1])
            vals.append(values_machine[param1])
            index_increment = 2
            result = values_machine[param1]
        elif current_value == 5:
            index = values_machine[param2] if values_machine[param1] != 0 else index + 3
            index_increment = 0
        elif current_value == 6:
            index = values_machine[param2] if values_machine[param1] == 0 else index + 3
            index_increment = 0
        elif current_value == 7:
            values_machine[param3] = (
                1 if values_machine[param1] < values_machine[param2] else 0
            )
        elif current_value == 8:
            values_machine[param3] = (
                1 if values_machine[param1] == values_machine[param2] else 0
            )

        index += index_increment


def perm_calc(vals, init=0, index_init={"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}):
    permutations = itertools.permutations(vals)
    high = 0
    for i in list(permutations):
        a = process([i[0], init])
        b = process([i[0], a])
        c = process([i[0], b])
        d = process([i[0], c])
        e = process([i[0], d])

        if e > high:
            high = e
    return high


main_loop = [4, 3, 2, 1, 0]
feedback_loop = [5, 6, 7, 8, 9]
print(perm_calc(main_loop))
