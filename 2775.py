import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())
    rooms = [[0 for _ in range(N)] for _ in range(K + 1)]
    for n in range(N):
        rooms[0][n] = n + 1
    for k in range(1, K + 1):
        for n in range(N):
            if n == 0:
                rooms[k][n] = rooms[k - 1][n]
            else:
                rooms[k][n] = rooms[k][n - 1] + rooms[k - 1][n]
    print(rooms[K][N - 1])
