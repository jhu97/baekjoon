import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
count = 0

for number in numbers:
    if number == 1:
        pass
    else:
        answer = []
        for n in range(2, number + 1):
            if number % n == 0:
                answer.append(n)
        if len(answer) == 1:
            count += 1

print(count)