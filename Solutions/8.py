def main():
    words = [word for word in input("inps: ").split(',')]
    words.sort()
    print(','.join(words))

if __name__ == "__main__":
    main()