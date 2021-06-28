import math


def prime_num(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

num_list = list(range(2, 123456*2))
emp_list = []

for i in num_list:
    if prime_num(i):
        emp_list.append(i)

n = int(input())

while n != 0:
    cnt = 0
    for i in emp_list:
        if n < i and i <= n * 2:
            cnt += 1
    print(cnt)
    n = int(input())
