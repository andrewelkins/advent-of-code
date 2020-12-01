# https://adventofcode.com/2019/day/7

import os
import itertools
import copy

values_raw = []
with open(os.path.join(os.path.dirname(__file__), "../../07/data.txt"), "r") as f:
    for line in f:
        values_raw = list(map(int, line.strip().split(",")))

values = {
    'a':copy.deepcopy(values_raw),
    'b':copy.deepcopy(values_raw),
    'c':copy.deepcopy(values_raw),
    'd':copy.deepcopy(values_raw),
    'e':copy.deepcopy(values_raw),
}

def process(vals, index=0, amp='a'):
    result = 0
    while True:
        if index >= len(values) - 1:
            break
        mode_string = str(f"{values[amp][index]:06}")

        param1 = 0
        param2 = 0
        param3 = 0

        try:
            param1 = values[amp][index + 1] if int(mode_string[-3]) == 0 else index + 1
            param2 = values[amp][index + 2] if int(mode_string[-4]) == 0 else index + 2
            param3 = values[amp][index + 3] if int(mode_string[-5]) == 0 else index + 3
        except IndexError:
            pass

        current_value = int(mode_string[-2:])
        index_increment = 4

        if current_value == 99:
            print("End.")
            return [result, index]
            break
        elif current_value == 1:
            values[amp][param3] = values[amp][param1] + values[amp][param2]
        elif current_value == 2:
            values[amp][param3] = values[amp][param1] * values[amp][param2]
        elif current_value == 3:
            values[amp][param1] = vals.pop(0)
            # values[amp][param1] = val
            index_increment = 2
        elif current_value == 4:
            print(values[amp][param1])
            vals.append(values[amp][param1])
            index_increment = 2
            result = values[amp][param1]
        elif current_value == 5:
            index = values[amp][param2] if values[amp][param1] != 0 else index + 3
            index_increment = 0
        elif current_value == 6:
            index = values[amp][param2] if values[amp][param1] == 0 else index + 3
            index_increment = 0
        elif current_value == 7:
            values[amp][param3] = 1 if values[amp][param1] < values[amp][param2] else 0
        elif current_value == 8:
            values[amp][param3] = 1 if values[amp][param1] == values[amp][param2] else 0

        index += index_increment


def perm_calc(vals, init=0, index_init={"a": [0,0], "b": [0,0], "c": [0,0], "d": [0,0], "e": [0,0]}):
    permutations = itertools.permutations(vals)
    high = 0
    for i in list(permutations):
        a = process([i[0], init], index_init['a'][1], 'a')
        print(a)
        b = process([i[1], a[0]], index_init['b'][1], 'b')
        c = process([i[2], b[0]], index_init['c'][1], 'c')
        d = process([i[3], c[0]], index_init['d'][1], 'd')
        e = process([i[4], d[0]], index_init['e'][1], 'e')
        if e[0] > high:
            high = e[0]
    return {"high":high, "index_init":{"a": a, "b": b, "c": c, "d": d, "e": e}}


l = [4, 3, 2, 1, 0]
main_loop = perm_calc(l)
print(main_loop['high'])
# feedback = [9, 8, 7, 6, 5]
# feedback_loop = perm_calc(feedback, main_loop['high'], main_loop['index_init'])
# print(feedback_loop['high'])
