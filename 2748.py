import sys
input = sys.stdin.readline
N = int(input())
F = [0, 1]
for n in range(2, N +1):
    Fn = F[n - 1] + F[n - 2]
    F.append(Fn)
print(F[N])
