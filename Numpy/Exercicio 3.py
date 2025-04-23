import numpy as np

arrayA = np.array([[2,5],[3,4]])

arrayB = np.array([[1,3],[4,0]])

arrayC = np.array([[2,5,3],[1,3,4],[0,2,1]])

arrayD = np.array([[2,5,3,1],[1,3,4,6],[0,2,1,5],[4,8,3,2]])

resultadoA = arrayA * arrayB

resultadoB = np.linalg.inv(arrayC)

resultadoC = np.linalg.det(arrayD)

print (resultadoA)

print (resultadoB)

print (resultadoC)