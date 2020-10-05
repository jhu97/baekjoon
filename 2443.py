import sys 
input = sys.stdin.readline
N = int(input())
for n in range(N, 0, -1):
    print("{0:>{1}}".format('*' * (2 * n - 1), N + n - 1 ))
