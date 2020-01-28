def main():
    first = openFile("train.3.txt")
    # TODO crea altre funzioni per creare il dataset e sposta il main


def openFile(name):
    f = open(name, "r")
    testList = []
    for itr in f:
        tmp = [float(n) for n in itr.split(',')]
        testList.append(tmp)
    f.close()
    print(len(testList))
    return testList


def dualPerceptron():
    # TODO finisci di implementarlo
    alfa = 0
    b = 0
    R = max()
    errors = 0
    while True:
        if errors == 0:
            break
    return alfa, b


if __name__ == '__main__':
    main()
