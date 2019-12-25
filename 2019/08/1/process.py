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
fewest = []
fewest_count = -1
for x in parts:
    zeros = x.count(0)
    if fewest_count == -1 or zeros < fewest_count:
        fewest_count = zeros
        fewest = x

print(fewest.count(1) * fewest.count(2))
