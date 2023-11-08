#!/bin/python3

# https://www.hackerrank.com/challenges/bon-appetit/problem

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    correct_bill = (sum(bill) - bill[k]) / 2
    if correct_bill == b:
        print('Bon Appetit')
    else:
        extra_amount_paid = int(sum(bill) / 2 - correct_bill)
        print(extra_amount_paid)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
