import sys
input = sys.stdin.readline
N = int(input())
for n in range(N):
    print("{0:>{1}}".format((2 * n + 1) * '*',N + n))
for i in range(N - 1, 0, -1):
    print("{0:>{1}}".format((2 * i - 1) * '*', N + i -1))
