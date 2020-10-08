import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    s = int(input())
    n = int(input())
    two = 0
    for N in range(n):
        q, p = map(int, input().split())
        two += q * p
    total = two + s
    print(total)
