# https://adventofcode.com/2019/day/3
import os


def read_values():
    with open(os.path.join(os.path.dirname(__file__), "../data.txt"), "r") as f:
        lines = []
        for line in f:
            lines.append(list(line.strip().split(",")))
        return lines


def increment_xy(data):
    map_plot = []
    xy = [0, 0]
    for i in data:
        for _ in range(0, int(i[1:])):
            map_plot.append(tuple(xy[:]))
            if i[0] == "U":
                xy[1] += 1
            elif i[0] == "D":
                xy[1] -= 1
            elif i[0] == "L":
                xy[0] -= 1
            elif i[0] == "R":
                xy[0] += 1
            else:
                print("data error")
                break

    return map_plot


def process(data):
    map_plot_1 = increment_xy(data[0])
    map_plot_2 = increment_xy(data[1])
    intersect = list(set(map_plot_1).intersection(set(map_plot_2)))
    abs_intersects = []
    for s in intersect:
        abs_intersects.append((abs(s[0]), abs(s[1])))
    sums = []
    for i in abs_intersects:
        if i == (0, 0):
            continue
        sums.append(sum(i))
    return min(sums)


print(process(read_values()))
