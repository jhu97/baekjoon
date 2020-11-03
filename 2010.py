import sys
input = sys.stdin.readline
N = int(input())
codes = []
numbers = 0
for _ in range(N):
    code = int(input())
    codes.append(code)
for i in range(N - 1):
    numbers += codes[i] - 1
numbers += codes[-1]
print(numbers)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
numbers = 1
for _ in range(N):
    code = int(input())
    numbers += code - 1
print(numbers)
