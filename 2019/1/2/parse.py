#https://adventofcode.com/2019/day/1#part2

import os
import math
import copy

def calulate_fuel(fuel):
    return math.floor(int(fuel) / 3) - 2

output = []
with open("../1/data.txt", "r") as f:
   for line in f:
       fuel = calulate_fuel(line.strip())
       current_fuel = calulate_fuel(copy.deepcopy(fuel))
       while current_fuel > 0:
           fuel += current_fuel
           current_fuel = calulate_fuel(current_fuel)
       output.append(fuel)

print(sum(output))