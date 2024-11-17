R = [(1,2)]
U = [(2,1),(3,1)]
counter = 0 
for x1,y1 in R :
    for x2,y2 in U :
        if x1-x2 == y2-y1 : 
            counter +=1

print (counter)