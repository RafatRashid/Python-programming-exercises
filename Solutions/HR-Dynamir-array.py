def query_1(sequence, y):
    sequence.append(y)


def query_2(sequence, y):
    return sequence[y % len(sequence)]


def main():
    inputs = input().split(' ')
    N = int(inputs[0])   # array size
    Q = int(inputs[1])   # test cases
    last_answer = 0
    seq_list = [([] * N) for x in range(N)]

    for each in range(Q):
        query_string = input().split(" ")

        query = int(query_string[0])
        x = int(query_string[1])
        y = int(query_string[2])

        index = (x ^ last_answer) % N

        if query == 1:
            query_1(seq_list[index], y)

        elif query == 2:
            last_answer = query_2(seq_list[index], y)
            print(last_answer)

if __name__ == "__main__":
    main()