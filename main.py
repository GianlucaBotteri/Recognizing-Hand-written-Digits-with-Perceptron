import function


def main():
    firstDigit = "9"
    secondDigit = "3"
    first = function.openFile("train." + firstDigit + ".txt")
    second = function.openFile("train." + secondDigit + ".txt")
    # TODO crea altre funzioni per creare il dataset e sposta il main
    dataset = function.createDataset(first, second)


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
