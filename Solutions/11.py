def main():
    binary_numbers = [x for x in input().split(',')]
    result = []
    for number in binary_numbers:
        temp = int(number, base = 2)
        if temp % 4 == 0:
            result.append(number)

    print(','.join(result))

if __name__ == "__main__":
    main()