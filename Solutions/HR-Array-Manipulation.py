import datetime


if __name__ == "__main__":
    start = datetime.datetime.now().time()
    for i in range(200001):
        i = i
        # print("operation", i, "performing...")

    stop = datetime.datetime.now().time()
    print(start, stop)
