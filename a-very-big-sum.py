import os


def aVeryBigSum(ar):
    sum = 0
    for value in ar:
        sum += value
    return sum


if __name__ == '__main__':

    fptr = open('new.txt', 'w')
    ar_count = int(raw_input())
    ar = map(long, raw_input().rstr
    result=aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
