import sys
import math
input = sys.stdin.readline

A, B, V = map(int, input().split())
N = (V - B) / (A - B)
if N == math.floor(N):
    print(int(N))
else:
    print(int(math.floor(N) + 1))
