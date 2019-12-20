# Advent of code - 2019 Day 4
# https://adventofcode.com/2019/day/4

from itertools import groupby, starmap
from operator import le


def has_adjacent(num):
    return if 2 in [len(list(g)) for _, g in groupby(list(str(num)))]
    # for _, g in groupby(list(str(num))):
    #     if len(list(g)) == 2:
    #         return True


def reduce_numbers(values):
    return [x for x in values if has_adjacent(x)]


def check_increasing(nums):
    return all(starmap(le, zip(nums, nums[1:])))


def process(start, stop):
    return len(
        [
            x
            for x in reduce_numbers(range(start, stop + 1))
            if check_increasing(list(str(x)))
        ]
    )


print(process(145852, 616942))
