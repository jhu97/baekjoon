import sys
input = sys.stdin.readline

N = int(input())

def factorial(N):
    total = 1
    if N != 0:
        for i in range(1, N):
            n = i % N
            total *= n
        total *= N
        print(total)
    else:
        print(total)

factorial(N)
