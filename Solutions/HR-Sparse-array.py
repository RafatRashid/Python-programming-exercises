if __name__ == "__main__":
    N = int(input())
    strings = []
    for i in range(N):
        strings.append(input())

    Q = int(input())
    for i in range(Q):
        query = input()
        counter = 0
        for j in strings:
            if query == j:
                counter += 1

        print(counter)
