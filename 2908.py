import sys
input = sys.stdin.readline

S = list(input().split())
new = ['','']
for i in range(2):
    for j in range(2, -1, -1):
        new[i] += S[i][j]

print(max(new))