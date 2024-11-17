import random
import sys 

sys.set_int_max_str_digits(1000000000) 
def find_k(a):
    number = 1
    k = 1
    while k <= 1000000:
        if a % 5 == 0 or a % 2 == 0 or a == 0 :
            print (-1)
            return
        if number % a == 0:
            ar = int(number//a)
            print(ar)
            return
        number = number * 10 + 1
        k += 1

# a = random.randint(0,100000)
# print(a)
a = int(input())
find_k(a)