import math
f,s,g,u,d = 1000000,20,1000000,2,4
counter = 0

if (abs(g-s))%( math.gcd(u,d)) == 0:
    if (s + u > f) and (s - d <= 0) :
        print ("imposible")
    elif (s > g and  d == 0) or (s < g and u == 0):
        print ("imposible")
    else:
        a = 1
        while a == 1 : 
            if s == g :
                print (counter)
                a = 0 
            elif s + u > f : 
                s -= d
                counter +=1
            elif s - d < 0 :
                s += d
                counter +=1
            elif s < g:
                s += u
                counter +=1
            elif s > g:
                s-=d
                counter =+1
else: 
    print ("imposible")

