import math
import function


def computeR(examples):
    modules = []
    for l in range(len(examples)):
        mod = 0
        for i in range(256):
            mod += math.pow((examples[l])[i], 2)
        modules.append(math.sqrt(mod))
    R = max(modules)
    return R


def dualFormPerceptron(dataset, R, gamma):
    b = 0
    examples = list(dataset.keys())
    alfa = [0] * len(examples)
    errors = -1  # Inizializzo il numero di errori ad un valore fittizio per entrare nel ciclo while
    iterations = 0
    while errors != 0:
        errors = 0  # Azzero il numero di errori prima dell'esecuzione del ciclo for
        for i in range(len(examples)):
            summation = 0
            for j in range(len(examples)):
                module = 0
                for k in range(len(examples[j])):  # In questo dataset sarà sempre 256
                    module += math.pow((examples[j])[k] - (examples[i])[k], 2)
                summation += alfa[j]*dataset[examples[j]]*math.exp(-gamma*module)  # Calcola la sommatoria per ogni j
            if dataset[examples[i]]*(summation+b) <= 0:  # Controlla se la classificazione è sbagliata
                alfa[i] += 1
                b += dataset[examples[i]]*math.pow(R, 2)
                errors += 1  # Incremento il numero di errori
        iterations += 1
    return alfa, b, iterations


def testPerceptron(testData, alfa, b, gamma):
    tests = list(testData.keys())
    errors = 0
    for i in range(len(tests)):
        summation = 0
        for j in range(len(tests)):
            module = 0
            for k in range(len(tests[j])):
                module += math.pow((tests[j])[k] - (tests[i])[k], 2)
            summation += alfa[j] * testData[tests[j]] * math.exp(-gamma * module)
        if testData[tests[i]] != function.sgn(summation+b):
            errors += 1
    return errors
