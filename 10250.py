import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    rooms = []
    for w in range(1, W + 1):
        w = str(w)
        w = w.zfill(2)
        for h in range(1, H + 1):
            h = str(h)
            room = h + w
            rooms.append(int(room))
    print(int(rooms[N - 1]))