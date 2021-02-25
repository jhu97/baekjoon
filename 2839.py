import sys
input = sys.stdin.readline

N = int(input())

answer = -1
for i in range(5):
  if N >= 3 * i and (N - 3 * i) % 5 == 0:
    answer = (N - 3 * i) // 5 + i
    break
print(answer)