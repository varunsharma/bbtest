import sys
import os

def factorial(num):
    if num == 0 :
        return 1
    return num*factorial(num-1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        print factorial(num)
