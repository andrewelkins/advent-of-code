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
        for a in range(0, int(i[1:])):
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
            map_plot.append(tuple(xy[:]))

    return map_plot


def process(data):
    map_plot_1 = increment_xy(data[0])
    map_plot_2 = increment_xy(data[1])
    intersections = set(map_plot_1) & set(map_plot_2)
    # much simpler answer for part 1
    # min(abs(x) + abs(y) for (x, y) in intersections)
    # +2 for the start and end points
    return min(sum(line.index(intersect) for line in [map_plot_1, map_plot_2]) for intersect in intersections) + 2


print(process(read_values()))
