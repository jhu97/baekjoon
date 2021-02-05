import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    numbers = list(map(int, input().split()))
    N = numbers[0]
    mean = sum(numbers[1:]) / N
    over = 0
    for number in numbers[1:]:
        if number > mean:
            over += 1
    percent = (over / N) * 100
    print('{0:0.3f}'.format(percent) + '%')
