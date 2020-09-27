import sys
input = sys.stdin.readline
total = int(input())
sum = 0
for i in range(9):
    money = int(input())
    sum += money
print(total - sum)
