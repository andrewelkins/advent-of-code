#https://adventofcode.com/2019/day/1

import os
import math

output = []
with open(os.path.join(os.path.dirname(__file__), "data.txt"), "r") as f:
   for line in f:
       b = math.floor(int(line.strip()) / 3) - 2
       output.append(b)

result = sum(output)
print(result)