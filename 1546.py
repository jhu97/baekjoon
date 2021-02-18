import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
biggest = max(scores)
total = 0
for n in scores:
    total += n / biggest * 100
mean = total / N
print(mean)