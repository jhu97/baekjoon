T= int(input())
for _ in range(T):
    N = int(input())
    S_D = {}
    for n in range(N):
        S, L = input().split()
        L = int(L)
        S_D[L] = S
    M = max(S_D.keys())
    print(S_D[M])
