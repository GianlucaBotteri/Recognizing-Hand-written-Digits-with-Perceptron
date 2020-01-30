import random

def openFile(name):
    f = open(name, "r")
    testList = []
    for itr in f:
        tmp = [float(n) for n in itr.split(',')]
        testList.append(tmp)
    f.close()
    print(len(testList))
    return testList


def createDataset(firstList, secondList):
    firstDict = {tuple(x): 1 for x in firstList}
    secondDict = {tuple(y): -1 for y in secondList}
    firstDict.update(secondDict)

    keyList = list(firstDict.keys())
    random.shuffle(keyList)

    dataset = {i: firstDict[i] for i in keyList}
    return dataset