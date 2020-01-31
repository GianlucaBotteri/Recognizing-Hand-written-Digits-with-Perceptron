import function
import perceptron


def main():
    firstDigit = "1"
    secondDigit = "7"
    print("Il primo carattere è:", firstDigit)
    print("Il secondo carattere è:", secondDigit)

    first = function.openTrainFile("train." + firstDigit + ".txt")
    second = function.openTrainFile("train." + secondDigit + ".txt")

    dataset = function.createDataset(first, second)

    examples = list(dataset.keys())
    R = perceptron.computeR(examples)
    gamma = 2
    alfa, b = perceptron.dualFormPerceptron(dataset, R, gamma)

    testAll = function.openTestFile("zip.test.txt")
    test = function.cutTest(testAll, firstDigit, secondDigit)
    length = len(test)
    print("Gli esempi del testing sono:", length)
    err = perceptron.testPerceptron(test, alfa, b, gamma)
    print("Il numero di errori in fase di test è:", err)
    print("La percentuale di errori è del:", err/length, "%")


if __name__ == '__main__':
    main()
