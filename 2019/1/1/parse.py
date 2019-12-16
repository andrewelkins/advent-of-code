import os
import math

output = []
with open("data.txt", "r") as f:
   for line in f:
       b = math.floor(int(line.strip()) / 3) - 2
       output.append(b)

result = sum(output)
print(result)