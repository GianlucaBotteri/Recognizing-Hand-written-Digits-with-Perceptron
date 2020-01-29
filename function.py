def openFile(name):
    f = open(name, "r")
    testList = []
    for itr in f:
        tmp = [float(n) for n in itr.split(',')]
        testList.append(tmp)
    f.close()
    print(len(testList))
    return testList
