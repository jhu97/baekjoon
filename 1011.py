import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    z = y - x
    count = 0
    for k in range(1, z + 1):
        if z >= (k ** 2 - k + 1) and z < (k ** 2 + 1):
            count = 2 * k - 1
        elif (k ** 2 + 1) <= z and z < (k ** 2 + k + 1):
            count = 2 * k
        if count != 0:
            break
    print(count)
