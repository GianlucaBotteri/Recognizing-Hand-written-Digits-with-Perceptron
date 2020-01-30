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
    print("Il valore di R è: ", R)
    alfa = [0] * len(examples)
    while True:
        errors = 0
        for i in range(len(examples)):
            summation = 0
            for j in range(len(examples)):
                sub = []
                module = 0
                for k in range(256):
                    sub.append((examples[j])[k] - (examples[i])[k])
                for k in range(256):
                    module += math.pow(sub[k], 2)
                summation += alfa[j]*dataset[examples[j]]*math.exp(-gamma*module)
            if dataset[examples[i]]*(summation+b) <= 0:
                alfa[i] += 1
                b += dataset[examples[i]]*math.pow(R, 2)
                errors += 1
        if errors == 0:
            break
    print(alfa)
    print(b)
    return alfa, b
