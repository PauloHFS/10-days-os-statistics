import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    S = []
    for i in range(len(values)):
        value = values[i]
        freq = freqs[i]

        S.extend([value for j in range(freq)])

    arr_aux = sorted(S)
    n = len(arr_aux)

    sub_arrs = [arr_aux[:n//2], arr_aux[(n+1)//2:]]
    quartiles_arr = []

    for array in sub_arrs:
        n = len(array)

        if n % 2 == 0:
            median = (array[n//2] + array[(n//2)-1]) / 2
        else:
            median = array[(n-1)//2]

        quartiles_arr.append(median)

    inter_quartile = quartiles_arr[1] - quartiles_arr[0]

    print(f'{inter_quartile:.1f}')


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
