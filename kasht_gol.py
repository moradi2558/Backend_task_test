a=[2,2]

n, m = 2,3

for i in range(0,max(n,m)):
    a.append(a[i-1] + a[i - 2])

result = a[m] + a[n] - 2 

print(result)