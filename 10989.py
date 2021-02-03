import sys
input = sys.stdin.readline

N = int(input())

numbers = [0] * 10001

for _ in range(N):
    number = int(input())
    numbers[number] += 1

for idx, val in enumerate(numbers):
    if val >= 1:
        for _ in range(val):
            print(idx)
