import sys
input = sys.stdin.readline

N = int(input())
count = 0

if N < 10:
    N = str(N)
    N = N.zfill(2)
else:
    N = str(N)
    
new = N
N = int(N)
if N == 0:
    count += 1
else:
    while True:
        N1, N2 = int(new[0]), int(new[1])
        total = str(N1 + N2)
        new = str(N2) + total[-1]
        count += 1
        if N == int(new):
            break

print(count)
