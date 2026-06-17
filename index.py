from time import
from math import

def timer(a):
    print("timer()")
    while a >= 0:
        print(a)
        a = a-1
        sleep(1)
    return a
