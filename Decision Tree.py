import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

dataset = pd.read_csv('movie.csv')
#print(dataset.to_string())

#numpy array of names of columns
colNames = list(dataset.columns.values)
#print (colNames)
#convert to numpy array
X = dataset.iloc[:, :].values   #original
#insert names of columns into the numpy array of data
X = np.insert(X, 0, colNames, 0)

rows = X.shape[0]
cols = X.shape[1]

for i in range (rows):
    print (X[i])

print()
print()

class node(object):
    def __init__(self):
        self.value = None
        self.decision = None
        self.child = None

def calculateEntropy(entropyList, cols):

    positive = 0
    negative = 0
    features = cols-1     #no of features including the target
    entropy = 0

    #calculate number of positive and negative samples
    for i in range(len(entropyList)):
        if entropyList[i][features] == 1:
            positive = positive + 1
        else:
            negative = negative + 1

    x = positive / (positive + negative)    #potion of data with +ve samples
    y = negative / (positive + negative)    #potion of data with +ve samples

    if x != 0 and y != 0:
        entropy = -1 * (x * math.log2(x) + y * math.log2(y))

    return entropy

def findMaxGain(dataset, rows, cols):

    #find if we have reached the leaf node
    yes = 0
    no = 0
    for a in range(1, rows):
        if (dataset[a][cols-1] == 1):
            yes = yes+1
        else:
            no = no+1

    if (yes == rows-1):
        return 0, -1, 1
    elif (yes == 0):
        return 0, -1, 0

    entropies = []
    #for each feature
    for j in range (cols-1):
        dict = {}
        #print ("NewDic")
        features = j

        #for each feature(col), store and count the no of groups/categories in it
        for i in range (1, rows):
            key = dataset[i][features]
            if key not in dict:
                dict[key] = 1
            else:
                dict[key] = dict[key] + 1

        featureEntropy = 0
        for key in dict:
            positive = 0
            negative = 0
            count = 0
            entropyList = []
            #for each column/category
            for k in range(1, rows):
                if dataset[k][j] == key:
                    count = count + 1
                    #print ("dataset[k]", dataset[k])
                    entropyList.append(dataset[k])

            keyEntropy = calculateEntropy(entropyList, cols)
            featureEntropy = featureEntropy + (count/(rows-1))*(keyEntropy)

        entropies.append(featureEntropy)

    infoGain = []
    for i in range (len(entropies)):
        infoGain.append(1 - entropies[i])

    #for i in range (len(infoGain)):
    #    print (infoGain[i])

    max = infoGain[0]
    index = 0

    for i in range (len(infoGain)):
        if (infoGain[i] > max):
            max = infoGain[i]
            index=i

    return max, index, -1

def buildTree(data, rows, cols):

    maxGain, index, leaf = findMaxGain(data, data.shape[0], data.shape[1])
    #print ("Maxgain index", maxGain, index, leaf)

    root = node()
    root.child = []

    if maxGain == 0:
        if leaf == 1:
            root.value = '1'
        else:
            root.value = '0'
        return root

    root.value = data[0][index]
    dict = {}

    for i in range(1, rows):
        key = data[i][index]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] += 1

    for key in dict:
        newrows = []
        newrows.append(data[0])
        for i in range (1, rows):
            if data[i][index] == key:
                newrows.append(data[i])

        #for a in range(len(newrows)):
        #    print(newrows[a])

        newrows = np.array(newrows)
        newrows = np.delete(newrows, index, 1)

        #for a in range(len(newrows)):
        #    print(newrows[a])

        temp = buildTree(newrows, newrows.shape[0], newrows.shape[1])
        temp.decision = key
        root.child.append(temp)
    return root

def traverse(root, level):

    print("Decision ", level, " ", root.decision)
    print("Value    ", level, " ", root.value)

    n = len(root.child)
    if n > 0:
        for i in range(0, n):
            traverse(root.child[i], level+1)

def predict(sample, root):

    print()
    #print("Decision",root.decision)
    #print("Value",  root.value)

    node = root
    while (1>0):
        for i in range (len(colNames)):
            #print (node.value, colNames[i])
            if node.value == colNames[i]:
                break

        #index = sample[i]
        #print("sample", sample[i])
        size = len(node.child)

        child = node.child[0]
        for n in range(0, size):
            child = node.child[n]
            #print(child.decision, sample[i])
            if (sample[i] == child.decision):
                break

        #print ("childvalue", child.value, child.decision)

        if child.value == '0':
            return 0

        if child.value == '1':
            return 1

        node = child

root = buildTree(X, rows, cols)
root.decision = 'Decision Tree Root'
traverse(root, 0)

print()
print("PREDICT")
print()

sample = ['US',	'yes',	'scifi',	'1']
sample2 = ['US', 'no',	'comedy',	'0']

#print ("Predicted value", predict(sample, root))
#print ("actual value", sample[cols-1])

#print ("Predicted value", predict(sample2, root))
#print ("actual value", sample2[cols-1])




