import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

number = [0 for _ in range(10)]

total = str(A * B * C) 

numbers = set(total)

for i in numbers:
    number[int(i)] = total.count(i)

for n in number:
    print(n)