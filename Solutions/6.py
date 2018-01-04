import math


def main():
    comma_seperated_inputs = input()
    D = [int(value) for value in comma_seperated_inputs.split(",")]
    result = []
    C = 50
    H = 30

    for each in D:
        # trunc() == rounding a number
        result.append(math.trunc(math.sqrt((2 * C * each) / H)))
    print(result)

if __name__ == "__main__":
    main()