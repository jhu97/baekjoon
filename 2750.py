import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for n in range(N):
    number = int(input())
    numbers.append(number)
    
numbers.sort()

for i in numbers:
    print(i)
