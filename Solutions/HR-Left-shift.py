if __name__ == "__main__":
    n, d = input().split(' ')
    array_size, rotations = [int(n), int(d)]
    half_size = int(array_size / 2)

    array = [int(x) for x in input().split(" ")]
    temp = []
    for i in range(array_size):
        temp.append(array[(i+rotations)%array_size])

    print(' '.join([str(x) for x in temp]))
