A = [2,1,1,3,2]
A.sort()

up = []
down = []

up.append(A[0])
up.append(A[-1])

down.append(A.pop(0))
down.append(A.pop())

i = 0
while i < len(A) - 2:
    if A[i] == A[i+1] == A[i+2]:
        A.pop(i)
    else:
        i += 1

for i in range(0, len(A)-1):
    up.append(A[i])
    down.append(A[i+1])

up = list(set(up))
down = list(set(down))

up.sort()
down.sort()

max_temp_up  = 0
max_temp_down = 0 

for i in range(len(up)-1,-1,-1):
    temp = up[i] - up [i-1]
    if max_temp_up < temp : 
        max_temp_up = temp

for i in range(len(down)-1,-1,-1):
    temp_d = down[i] - down [i-1]
    if max_temp_down < temp_d : 
        max_temp_down = temp_d

if max_temp_up > max_temp_down :
     print(max_temp_up)
else:
    print(max_temp_down)
