import sys
input = sys.stdin.readline
N = int(input())
for n in range(N, 0, -1):
    print("{0:>{1}}".format((2 * n - 1) * '*', N + n - 1))
for i in range(2, N + 1, 1):
    print("{0:>{1}}".format((2 * i - 1) * '*', N + i - 1))
