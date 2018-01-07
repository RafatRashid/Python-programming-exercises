import re


def main():

    eligible_passwords = []
    input_string = input().split(",")
    for password in input_string:

        if len(password) < 6 or len(password) > 12:
            continue
        elif not re.search(pattern="[A-Z]", string=password):
            continue
        elif not re.search(pattern="[a-z]", string=password):
            continue
        elif not re.search("[$#@]", password):
            continue
        elif not re.search("[0-9]", password):
            continue

        eligible_passwords.append(password)

    print(','.join(eligible_passwords))

if __name__ == "__main__":
    main()