import function
import perceptron


def main():
    firstDigit = "5"
    secondDigit = "6"
    first = function.openFile("train." + firstDigit + ".txt")
    second = function.openFile("train." + secondDigit + ".txt")
    dataset = function.createDataset(first, second)

    examples = list(dataset.keys())
    R = perceptron.computeR(examples)
    gamma = 0.5
    dualFormPerceptron(dataset, R, gamma)


def dualFormPerceptron(dataset, R, gamma):
    b = 0
    examples = list(dataset.keys())
    print(R)
    alfa = [0] * len(examples)
    while True:
        errors = 0
        if errors == 0:
            break
    return alfa, b


# TODO creare funzione testPerceptron

if __name__ == '__main__':
    main()
