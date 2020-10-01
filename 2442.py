import sys
input = sys.stdin.readline
N = int(input())
for n in range(N):
    print("{0:>{1}}".rstrip().format((2 * n + 1) * '*', N + n))
