import numpy as np

arrayA = np.arange(1, 6)

arrayB = np.arange(1, 6)

arrayC = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

resultadoA = arrayA + arrayB

resultadoB = np.multiply.outer(arrayA, arrayC)

print(resultadoA)

print(resultadoB)
