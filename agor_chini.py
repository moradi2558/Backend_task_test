import numpy as np

n = 3 
matrix = np.zeros((n, n+1))

def dp(matrix,i,j,n):
    if j == 0 or i == n-1 : 
        return 1
    else :
        x = n 
        y = j-1
        counter = 0 
        while x >= j-1 and y >= 0 :
            counter +=1
            x-=1
            y-=1
        return counter

for i in range (n-1,-1,-1):
    for j in range (0,n+1):
        matrix[i,j] = dp(matrix,i,j,n)


def result(i,j,matrix) :
    x = j - 1
    y = i-1
    counter = 0 
    while x >= 0 :
        counter += matrix[x,y]
        x-=1
        y-=1
    return counter

result = result(n,n,matrix)
# matrix[0,n] = result
# print(matrix)
print (result)