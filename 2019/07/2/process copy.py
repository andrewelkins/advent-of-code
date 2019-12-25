# https://adventofcode.com/2019/day/7

import os
import itertools

values = []
with open(os.path.join(os.path.dirname(__file__), "../../07/data.txt"), "r") as f:
    for line in f:
        values = list(map(int, line.strip().split(",")))


def process(vals, index=0):

    result = 0
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
            # print("End.")
            return [result, index]
            break
        elif current_value == 1:
            values[param3] = values[param1] + values[param2]
        elif current_value == 2:
            values[param3] = values[param1] * values[param2]
        elif current_value == 3:
            values[param1] = vals.pop(0)
            # values[param1] = val
            index_increment = 2
        elif current_value == 4:
            print(values[param1])
            vals.append(values[param1])
            index_increment = 2
            result = values[param1]
        elif current_value == 5:
            index = values[param2] if values[param1] != 0 else index + 3
            index_increment = 0
        elif current_value == 6:
            index = values[param2] if values[param1] == 0 else index + 3
            index_increment = 0
        elif current_value == 7:
            values[param3] = 1 if values[param1] < values[param2] else 0
        elif current_value == 8:
            values[param3] = 1 if values[param1] == values[param2] else 0

        index += index_increment


def perm_calc(vals, init=0, index_init={"a": 0, "b": 0, "c": 0, "d": 0, "e": 0}):
    # permutations = itertools.permutations(vals)
    permutations = vals
    high = 0
    a = b = c = d = e = [0, 0]
    for i in list([permutations]):
        a = process([i[0], init])
        b = process([i[0], b])
        c = process([i[0], c])
        d = process([i[0], d])
        e = process([i[0], e])

        if e[0] > high:
            high = n
    return {"high": high, "index_init": {"a": a, "b": b, "c": c, "d": d, "e": e}}


main_loop = [4, 3, 2, 1, 0]
feedback_loop = [5, 6, 7, 8, 9]
main_loop_result = perm_calc(main_loop, 0)
feedback_loop_result = perm_calc(
    feedback_loop["high"], 880726, feedback_loop["index_init"]
)
print(feedback_loop_result)
# if main_loop_result == 880726:
#     print(main_loop_result)
#     print(perm_calc(feedback_loop, main_loop_result))
# else:
#     print("Error in main logic")
