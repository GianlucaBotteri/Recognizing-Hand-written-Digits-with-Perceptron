import random


def openTrainFile(name):
    file = open(name, "r")
    valueList = []
    for itr in file:
        tmp = [float(n) for n in itr.split(',')]
        valueList.append(tmp)
    file.close()
    return valueList


def openTestFile(name):
    file = open(name, "r")
    valueList = []
    for itr in file:
        tmp = [float(n) for n in itr.split(' ')]
        valueList.append(tmp)
    file.close()
    return valueList


def cutTest(testAll, fDigit, sDigit):
    testFirst = []
    testSecond = []
    for i in range(len(testAll)):
        if (testAll[i])[0] == int(fDigit):
            testFirst.append((testAll[i])[1:])
        if (testAll[i])[0] == int(sDigit):
            testSecond.append((testAll[i])[1:])
    return createDataset(testFirst, testSecond)


def createDataset(firstList, secondList):
    firstDict = {tuple(x): 1 for x in firstList}
    secondDict = {tuple(y): -1 for y in secondList}
    firstDict.update(secondDict)

    keyList = list(firstDict.keys())
    random.shuffle(keyList)

    dataset = {i: firstDict[i] for i in keyList}
    return dataset


def sgn(x):
    if x >= 0:
        return 1
    return -1
