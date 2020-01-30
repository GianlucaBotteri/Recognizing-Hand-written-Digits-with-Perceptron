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
