# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
def miniMaxSum(arr):
    max = None
    min = None
    sum = 0
    for value in arr:
        if(max == None):
            max = value
        elif(max < value):
            max = value

        if(min == None):
            min = value
        elif(min > value):
            min = value

        sum += value

    print sum-max, sum-min


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
