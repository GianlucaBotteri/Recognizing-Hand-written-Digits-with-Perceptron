def main():
    first = openFile("train.0.txt")


def openFile(name):
    f = open(name, "r")
    testList = []
    for itr in f:
        itr.rstrip("\n")
        testList.append(itr)
    f.close()
    print(len(testList))
    return testList


if __name__ == '__main__':
    main()
