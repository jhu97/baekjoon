a, b = map(int, input().split())
if a >= b :
    a, b = b, a
GCD = 1
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        GCD = i
        break
LCM = (a // GCD) * (b // GCD) * GCD
print(GCD)
print(LCM) 
