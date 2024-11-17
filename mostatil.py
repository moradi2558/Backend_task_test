
def find_max_less_than_k(n, k, m, x, y):
    p = int(1e9 + 7) 
    max_value = 0 
    k2 = 0 
    premid = 0 
    mid = p // 2  
    postmid = p  

   
    while k2 != k:
        
        max_value = 0
        a = m 
        k2 = 0  

      
        for i in range(1, n + 1):
            if a < mid:
                k2 += 1
                if a > max_value:
                    max_value = a
            a = (a * x + y) % p

        if k2 > k:
            postmid = mid
        else:
            premid = mid
        
        mid = (postmid + premid) // 2  

    return max_value



n, k, m, x, y = map(int, input().split())


result = find_max_less_than_k(n, k, m, x, y)
print(result)
