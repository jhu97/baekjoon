T = int(input())
alphanumeric = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:'
for _ in range(T):
    R, S = input().split(' ')
    P = []
    for s in S:
        if s in alphanumeric:
            P.append(s * int(R))
    print(*P, sep='')
