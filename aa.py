import csv

with open('b.csv') as A:
    reader = csv.reader(A)
    for row in reader:
        A=[]
        A.append(row)
print(row)