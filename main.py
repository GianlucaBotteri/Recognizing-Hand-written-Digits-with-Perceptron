import matplotlib.pyplot as plt
import function
import perceptron


def main():
    firstDigit = "1"
    secondDigit = "7"
    print("Il primo carattere da riconoscere è:", firstDigit)
    print("Il secondo carattere da riconoscere è:", secondDigit)
    print(" ")

    # Vengono recuperati i dati per il training
    first = function.openTrainFile("res/"+"train." + firstDigit + ".txt")
    second = function.openTrainFile("res/"+"train." + secondDigit + ".txt")

    # Dataset di training, gli esempi sono in ordine casuale
    dataset = function.createDataset(first, second)

    testAll = function.openTestFile("res/"+"zip.test.txt")
    # Dataset di testing, include solo le due cifre utili
    test = function.cutTest(testAll, firstDigit, secondDigit)
    length = len(test)
    print("Gli esempi nel testing sono:", length)

    # Lista di tutti gli esempi nel dataset, senza il loro label
    examples = list(dataset.keys())
    R = perceptron.computeR(examples)  # Calcola il valore di R
    print("Il valore di R è:", R)
    gammaList = []  # Lista che terrà tutti i valori di gamma usati
    errorList = []  # Lista con il numero di errori per ogni valore di gamma
    # Lista che ricorda il numero di iterazione in fase di training per ogni gamma
    iterList = []

    for g in range(2, 38, 4):
        gammaList.append(g)
        print("Il valore di gamma è:", g)
        alfa, b, iterations = perceptron.dualFormPerceptron(dataset, R, g)
        err = perceptron.testPerceptron(test, alfa, b, g)
        print("Il numero di errori in fase di test è:", err)
        print("La percentuale di errori è del:", (err/length)*100, "%")
        errorList.append(err)
        iterList.append(iterations)

    plt.plot(gammaList, errorList)
    plt.xlabel("Valori di gamma")
    plt.ylabel("Numero di errori")
    plt.show()

    plt.plot(gammaList, iterList)
    plt.xlabel("Valori di gamma")
    plt.ylabel("Numero di iterazioni")
    plt.show()


if __name__ == '__main__':
    main()
