def can_swap(a, b):
    return bin(a ^ b).count('1') == 1

def sort(n, arr):
    size = 2 ** n
    swaps = []

    for i in range(size):
        for j in range(size - 1):
            if arr[j] > arr[j + 1]:
                if can_swap(j, j + 1):  
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                    swaps.append((j, j + 1)) 
    return swaps


n = int(input())
arr = list(map(int, input().split()))

swaps = sort(n, arr)

print(len(swaps))
for swap in swaps:
    print(swap[0], swap[1])

print(arr)


