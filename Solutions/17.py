def main():
    total_money = 0
    while True:
        log_string = input()
        if not log_string:
            break

        action = log_string.split(" ")
        if action[0] == 'D':
            total_money += int(action[1])
        elif action[0] == "W":
            total_money -= int(action[1])

    print(total_money)

if __name__ == "__main__":
    main()