import sys
input = sys.stdin.readline
N, X = map(int, input().split())
numbers = []
numbers[:N] = map(int, input().split())
for i in numbers:
    if i < X:
        print(i)
