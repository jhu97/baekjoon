import sys
input = sys.stdin.readline

N = int(input())
numbers = [0 for _ in range(2000001)]

for _ in range(N):
    number = int(input())
    numbers[number + 1000000] += 1

for idx, val in enumerate(numbers):
    if val == 1:
        print(idx - 1000000)
