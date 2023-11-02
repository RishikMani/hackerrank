#!/bin/python3

# https://www.hackerrank.com/challenges/the-birthday-bar/problem

import os

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    ways_to_divide = 0

    if len(s) == m and sum(s) == d:
        return 1

    for index in range(len(s[:-(m - 1)])):
        if sum(s[index:index+m]) == d:
            ways_to_divide += 1
    return ways_to_divide


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
