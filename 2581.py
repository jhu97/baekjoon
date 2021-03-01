import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
numbers = []

for n in range(M, N + 1):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    if count == 1:
        numbers.append(n)

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(numbers[0])