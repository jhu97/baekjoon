import sys
input = sys.stdin.readline
N = int(input())
for i in range(1, N + 1):
    print("{0}{1}{2}".format('*' * i, (2 * N - 2 * i) * ' ', '*' * i))
for n in range(N - 1, 0, -1):
    print("{0}{1}{2}".format('*' * n, (2 * N - 2 * n) * ' ', '*' * n))
