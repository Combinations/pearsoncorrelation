#Pearson Correlation
import numpy as np

def Normalize(vector):
    vectorSum = 0;
    for value in vector: 
           vectorSum = vectorSum + value;
    mean = vectorSum/len(vector)
    normalizedVector = vector - mean; 
    return normalizedVector

def ComputeSimilarity(x, y):
    numerator = np.dot(x,y)
    euclideanMagnitudeX = np.linalg.norm(x)
    euclideanMagnitudeY = np.linalg.norm(y)
    similarity = (numerator) /(euclideanMagnitudeX * euclideanMagnitudeY)
    return similarity

def Analyze():
        unitVector = [1,1]
        samples = np.array([[2,5],[2,1]])
        x = Normalize(samples[0])
        y = Normalize(samples[1])

        sim0 = ComputeSimilarity(unitVector,x)
        sim1 = ComputeSimilarity(unitVector, y)

        print(sim0)
        print(sim1)


Analyze()
