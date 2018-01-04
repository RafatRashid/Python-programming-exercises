def main():
    _input = [int(x) for x in input().split(',')]
    X = _input[0]
    Y = _input[1]
    result = []

    for i in range(0, X):

        column = []
        for j in range(0, Y):
            column.append(i * j)

        result.append(column)

    print(result)

if __name__ == "__main__":
    main()