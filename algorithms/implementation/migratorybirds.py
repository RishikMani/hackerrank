#!/bin/python3

# https://www.hackerrank.com/challenges/migratory-birds/problem

import os

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    arr.sort()
    birds_dict = dict()

    for bird in arr:
        birds_dict[bird] = birds_dict.get(bird, 0) + 1

    max_value = max(birds_dict.values())
    for k, v in birds_dict.items():
        if v == max_value:
            return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
