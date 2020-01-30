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
    gamma = 2
    perceptron.dualFormPerceptron(dataset, R, gamma)


# TODO creare funzione testPerceptron

if __name__ == '__main__':
    main()
