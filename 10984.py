import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    total = 0
    mean = 0
    for n in range(N):
        C, G = map(float, input().split())
        total += C
        mean += C * G
    mean = round(mean / total, 1)
    print(int(total), mean)
