if __name__ == "__main__":
    n, inputs = [int(n) for n in input().split(" ")]
    array = [0]*(n+1)

    for _ in range(inputs):
        x, y, incr = [int(n) for n in input().split(" ")]
        array[x-1] += incr
        if((y)<=len(array)):
            array[y] -= incr

    maximum = x = 0
    for i in list:
        x = x+i
        if maximum < x:
            maximum=x
    print(maximum)