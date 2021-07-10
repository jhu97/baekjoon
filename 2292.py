import sys
input = sys.stdin.readline

N = int(input())

n = 1

if N == 1:
    print(1)
else:
    while True:
        if (6 * n - 4 <= N) and (N <= 3 * (n ** 2) + 3 * n + 1):
            print(n + 1)
            break
        else:
            n += 1
'''
import sys
import math
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
else:
    print(int((3 + math.sqrt(12 * N -15)) // 6 + 1))
'''
