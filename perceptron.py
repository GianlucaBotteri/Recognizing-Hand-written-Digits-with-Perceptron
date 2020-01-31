import math


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
    while errors != 0:
        errors = 0  # Azzero il numero di errori prima dell'esecuzione del ciclo for
        for i in range(len(examples)):
            summation = 0
            for j in range(len(examples)):
                module = 0
                for k in range(256):  # 256 sono il numero di valori fissati per ogni esempio del dataset
                    module += math.pow((examples[j])[k] - (examples[i])[k], 2)
                summation += alfa[j]*dataset[examples[j]]*math.exp(-gamma*module)  # Calcola la sommatoria per ogni j
            if dataset[examples[i]]*(summation+b) <= 0:  # Controlla se la classificazione è sbagliata
                alfa[i] += 1
                b += dataset[examples[i]]*math.pow(R, 2)
                errors += 1  # Incremento il numero di errori
    print(alfa)
    print(b)
    return alfa, b
