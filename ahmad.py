# import random
# n= obj
# m= box
# k= volume
n, m, k = map(int, input().split())
# n=random.randint(1,9)
# print(n)
# m=random.randint(1,9)
# print(m)
# k=random.randint(1,9)
# print(k)
# boxes= [k] * m
numbers = input()
i = [int(num) for num in numbers.split()]
# i = n  
# min_value = 1  
# max_value =  9   

# i = [random.randint(min_value, max_value) for _ in range(n)]
# print(i)
s=0
t=0
j=n-1
limit = k 
while  j >= 0 and m > 0 :
    if limit - i[j] > -1:
        limit = limit - i[j]
        j -= 1
        s += 1
    else:
        limit = k
        m -= 1
        t += 1
print(s)







