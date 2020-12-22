import sys
input = sys.stdin.readline

N = int(input())
count_list = [0 for _ in range(8001)]
numbers = []
total = 0

for _ in range(N): 
    number = int(input())
    count_list[number + 4000] += 1
    total += number
    numbers.append(number)

mean = round(total / N)

numbers.sort()

median = numbers[N // 2]

difference = max(numbers) - min(numbers)

mode_list = []
biggest = max(count_list)

for index, y in enumerate(count_list):
    if y == biggest:
        mode_list.append(index - 4000)
    else:
        pass

if len(mode_list) == 1:
    mode = mode_list[0]
else:
    mode = mode_list[1]

'''
num_biggest = count_list.count(biggest)

mode = count_list.index(biggest) - 4000
if num_biggest > 1:
    mode = count_list.index(biggest, mode + 4001) - 4000
'''

print(mean)
print(median)
print(mode)
print(difference)
