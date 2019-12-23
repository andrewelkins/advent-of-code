# https://adventofcode.com/2019/day/6

import os


def process(data):
    count = 0
    for planet in data.keys():
        num_orbits = 1
        while data[planet] in data:
            num_orbits += 1
            planet = data[planet]
        count += num_orbits
    return count


orbit_data = {}
with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
    for line in f:
        # child > parent
        relation = line.strip().split(")")
        orbit_data[relation[1]] = relation[0]


print(process(orbit_data))
