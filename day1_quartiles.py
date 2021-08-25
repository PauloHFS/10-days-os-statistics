import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quartiles(arr):
    arr_aux = sorted(arr)
    n = len(arr_aux)

    sub_arrs = [arr_aux[:n//2], arr_aux, arr_aux[(n+1)//2:]]
    quartiles_arr = []

    for array in sub_arrs:
        n = len(array)

        if n % 2 == 0:
            median = (array[n//2] + array[(n//2)-1]) / 2
        else:
            median = array[(n-1)//2]

        quartiles_arr.append(int(median))

    return quartiles_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
