import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(N):
    S = input().rstrip()
    A = set(S)
    if len(S) == len(A):
        cnt += 1
    else:
        cnt1 = 0
        for a in A:
            if (S.count(a) * a) in S:
                cnt1 += 1
            else:
                break
        if cnt1 == len(A):
            cnt += 1

print(cnt)
