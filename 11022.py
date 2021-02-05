import sys
input = sys.stdin.readline

N = int(input())

for n in range(1, N + 1):
    A, B = map(int, input().split())
    total = A + B
    print('Case #{0}: {1} + {2} = {3}'.format(n, A, B, total))
