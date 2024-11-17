def back (n):
    if n > 4 :
        s = int (not (back(n-1) * back(n-4)) )
        return s
    elif n == 1 or n == 3 or n == 4: 
        return 1
    elif n == 2 :
        return 0
    
s = back(7)

print (s)
    