import math
import function


def computeR(examples):
    modules = []
    for l in range(len(examples)):
        mod = 0
        for i in range(examples[l]):
            mod += math.pow((examples[l])[i], 2)
        modules.append(math.sqrt(mod))
    R = max(modules)
    return R


def dualFormPerceptron(dataset, R, gamma):
    b = 0
    examples = list(dataset.keys())
    alfa = [0] * len(examples)
    # Inizializzo il numero di errori per entrare nel ciclo while
    errors = -1
    iterations = 0
    while errors != 0:
        errors = 0  # Azzero il numero di errori prima dell'esecuzione del ciclo
        for i in range(len(examples)):
            summation = 0
            for j in range(len(examples)):
                module = 0
                for k in range(len(examples[j])):  # In questo dataset sarà sempre 256
                    module += math.pow((examples[j])[k] - (examples[i])[k], 2)
                # Calcola la sommatoria per ogni j
                summation += alfa[j]*dataset[examples[j]]*math.exp(-gamma*module)
            # Controlla se la classificazione è sbagliata
            if dataset[examples[i]]*(summation+b) <= 0:
                alfa[i] += 1
                b += dataset[examples[i]]*math.pow(R, 2)
                errors += 1  # Incrementa il numero di errori
        iterations += 1
    return alfa, b, iterations


def testPerceptron(testData, trainData, alfa, b, gamma):
    tests = list(testData.keys())  # Esempi di test, senza etichetta
    trains = list(trainData.keys())  # Esempi di train, senza etichetta
    errors = 0
    for i in range(len(tests)):
        summation = 0
        for j in range(len(trains)):
            module = 0
            for k in range(len(trains[j])):
                module += math.pow((trains[j])[k] - (tests[i])[k], 2)
            summation += alfa[j] * trainData[trains[j]] * math.exp(-gamma * module)
        if testData[tests[i]] != function.sgn(summation+b):
            errors += 1
    return errors
