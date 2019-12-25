from copy import deepcopy
import os
import itertools


def layers(a_list, chuck_length):
    for x in range(0, len(a_list), chuck_length):
        yield a_list[x : x + chuck_length]


values = []
with open(os.path.join(os.path.dirname(__file__), "../../08/data.txt"), "r") as f:
    for line in f:
        values = list(map(int, list(line)))

chunk = 25 * 6
parts = layers(values, chunk)
results = []
start = 0
for x in parts:
    index = 0
    if start == 0:
        start = 1
        results = x
    for i in x:
        if results[index] == 2 and (i == 0 or i == 1):
            results[index] = i
        index += 1

for x in layers(results, 25):
    print(x)