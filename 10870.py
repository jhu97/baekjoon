n = int(input())
numbers = [0,1]

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while (len(numbers) - 1) < n:
        numbers.append(numbers[-2]+numbers[-1])
    print(numbers[-1])