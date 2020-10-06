import sys
input = sys.stdin.readline
N = int(input())
for n in range(1, N + 1):
    print("{0:>{1}}".format(n * '*', N))
for i in range(N - 1, 0, -1):
    print("{0:>{1}}".format(i * '*', N))
