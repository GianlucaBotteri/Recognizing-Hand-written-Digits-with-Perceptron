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


# cutTest rimuove dalla lista del testing le cifre non utilizzate, e poi ritorna chiamando createDataset
def cutTest(testAll, fDigit, sDigit):
    testFirst = []
    testSecond = []
    for i in range(len(testAll)):
        if (testAll[i])[0] == int(fDigit):
            testFirst.append((testAll[i])[1:])
        if (testAll[i])[0] == int(sDigit):
            testSecond.append((testAll[i])[1:])
    return createDataset(testFirst, testSecond)


# Questa funzione prende in ingresso due liste, associa ad ognuna un label e poi crea un dizionario
# in cui gli elementi delle liste sono mischiati tra loro, per non avere prima tutti gli 1 e poi -1
def createDataset(firstList, secondList):
    firstDict = {tuple(x): 1 for x in firstList}
    secondDict = {tuple(y): -1 for y in secondList}
    firstDict.update(secondDict)

    keyList = list(firstDict.keys())
    random.seed(2)  # Inizializzzo il seed per avere ad ogni run lo stesso shuffle
    random.shuffle(keyList)

    dataset = {i: firstDict[i] for i in keyList}
    return dataset


def sgn(x):
    if x >= 0:
        return 1
    return -1
