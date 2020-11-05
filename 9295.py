import sys
input = sys.stdin.readline
T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    add = a + b
    print("Case {0}: {1}".format(i, add))
