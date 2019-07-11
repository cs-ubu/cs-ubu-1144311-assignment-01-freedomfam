# import csv

# f = open('A.csv','r')
# A =[]
# for line in f.readline():
#     A.append([ float(x) for x in line.strip().split(',')])

# print(A)
# f.close()

# f = open('b.csv','r')
# b =[]
# for line in f.readline():
#     A.append([ float(x) for x in line.strip().split(',')])



def matmul(A,b):
    m,n = len(A) , len(b[0])
    J= len(A[0])
    if len(A[0]) == len(b):
        C = [ [0]*n for i in range(m) ]
        for r in range(m):
            for c in range(n):
                C[r][c] = sum([ A[c][j]*b[j][c] for j in range(J)])
            return C
        return []
mat = matmul(A,b)
print(mat)