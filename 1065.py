import sys
input = sys.stdin.readline

N = int(input())
n = 1
total = 0

while n <= N:
    if n < 100:
        total = n
    else:
        n = str(n)
        if (int(n[0]) - int(n[1])) == (int(n[1]) - int(n[2])):
            total += 1
        n = int(n)
    n += 1

print(total)