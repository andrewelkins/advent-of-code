# https://adventofcode.com/2019/day/6

import os


def process(data):
    orbit_path = {"SAN": [], "YOU": []}
    for planet in ["SAN", "YOU"]:
        source = planet
        while data[planet] in data:
            planet = data[planet]
            orbit_path[source].append(planet)
    count = 0
    for x in orbit_path["SAN"]:
        if x in orbit_path["YOU"]:
            count = count + orbit_path["YOU"].index(x)
            break
        count += 1

    return count


orbit_data = {}
with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
    for line in f:
        # child > parent
        relation = line.strip().split(")")
        orbit_data[relation[1]] = relation[0]


print(process(orbit_data))
