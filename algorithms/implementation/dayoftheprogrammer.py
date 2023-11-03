#!/bin/python3

# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

import os

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year <= 1917:
        if year % 4 ==0:
            return f'12.09.{year}'
        return f'13.09.{year}'
    elif year == 1918:
        return '26.09.1918'
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return f'12.09.{year}'
        return f'13.09.{year}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
