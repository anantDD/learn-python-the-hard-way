#!/bin/python

# import math
# import os
# import random
# import re
# import sys

# Complete the staircase function below.


def staircase(n):
    for i in range(n):
        # print space n-1-i times
        # print i+1 times asterisk
        line = ''
        for j in range(n):

            if (j < n-i-1):
                line += ' '
            else:
                line += '#'
        print line


if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
