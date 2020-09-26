Changyeong = 100
Sangduk = 100
n = int(input())
for _ in range(n):
    c, s = map(int, input().split())
    C_dice = [0 for i in range(6)]
    S_dice = [0 for i in range(6)]
    C_dice[c - 1] += 1
    S_dice[s - 1] += 1
    if C_dice.index(1) > S_dice.index(1):
        Sangduk -= c
    elif C_dice.index(1) < S_dice.index(1):
        Changyeong -= s
    else:
        pass
print(Changyeong)
print(Sangduk)

-----------------------------------------------------------

Changyeong = 100
Sangduk = 100
n = int(input())
for _ in range(n):
    c, s = map(int, input().split())
    if c > s:
        Sangduk -= c
    elif c < s:
        Changyeong -= s
    else:
        pass
print(Changyeong)
print(Sangduk)
