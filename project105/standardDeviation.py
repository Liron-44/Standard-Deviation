import math
import csv

with open('stdData.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    total = 0
    n = len(data)
    for a in data: 
       total+=int(a)
    mean = total/n
    return mean

squaredList = []

for number in data:
    b = int(number)- mean(data)
    b = b**2
    squaredList.append(b)

sum = 0

for c in squaredList:
    sum = sum+c

result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)
print(standardDeviation)