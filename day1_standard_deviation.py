import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/len(arr)

    sum_square_distance = 0
    for num in arr:
        sum_square_distance += (num - mean) ** 2

    standard_deviation = math.sqrt(sum_square_distance/len(arr))

    print(f'{standard_deviation:.1f}')


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
