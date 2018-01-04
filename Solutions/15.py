def main():
    a = input()
    arg1 = int("{}".format(a))
    arg2 = int("{}{}".format(a,a))
    arg3 = int("{}{}{}".format(a,a,a))
    arg4 = int("{}{}{}{}".format(a,a,a,a))

    print(arg1+arg2+arg3+arg4)

if __name__ == "__main__":
    main()