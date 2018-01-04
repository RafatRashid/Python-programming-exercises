def main():
    words = [x for x in input().split(' ')]
    non_duplicated_words = list(set(words))
    non_duplicated_words.sort()
    print(' '.join(non_duplicated_words))

if __name__ == "__main__":
    main()