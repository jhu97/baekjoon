import sys
import math

input = sys.stdin.readline

A, B, C = map(int, input().split())

if C > B:
    n = A / (C - B)
    if n > 0: 
        if math.floor(n) == n :
            print(int(n + 1))
        elif math.floor(n) < n:
            print(int(math.ceil(n)))
    else:
        print(-1)
else:
    print(-1)
