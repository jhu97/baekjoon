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
