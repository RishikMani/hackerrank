#!/bin/python3

# https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def turn_pages(p: int, page_index_per_turn: list, direction: str):
    # Look within `page_index_per_turn` where `p` is and return the index of
    # that item in the list.
    if direction == "back":
        page_index_per_turn.reverse()
    for idx, i in enumerate(page_index_per_turn):
        if isinstance(i, list) and p in i:
            return idx


def pageCount(n: int, p: int):
    # if `p` is the first or last page no page turn is needed
    if p == 1 or p == n:
        return 0

    # if there are odd pages and we need to see the page before the last page,
    # no page turn is needed, and we start from back. e.g. n=13, p=12
    if n % 2 != 0 and p == n - 1:
        return 0

    # Let's us record the page indexes on each turn in the form of a list.
    # e.g. first page is only `1`, second page is `[2, 3]`
    # if the last page is even, e.g. 20 then it is `20`,
    # but if the last page is 19, then indexes on that page will be `[18, 19]`
    page_index_per_turn = [1]
    for i in range(2, n, 2):
        page_index_per_turn.append([i, i + 1])
    if n % 2 == 0:
        page_index_per_turn.append(n)

    front = turn_pages(p, page_index_per_turn, "front")
    back = turn_pages(p, page_index_per_turn, "back")
    return min(front, back)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
