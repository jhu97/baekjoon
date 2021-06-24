import sys
input = sys.stdin.readline

a = [int(input()) for _ in range(9)]

for i,v in enumerate(a):
    if max(a) == v:
        print(v)
        print(i+1)