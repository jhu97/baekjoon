import sys
input = sys.stdin.readline
N = int(input())
rest = 0
for _ in range(N):
    students, apple = map(int, input().split())
    rest += apple % students
print(rest)
