N = int(input())
max_price = 0
for _ in range(N):
    numbers = list(map(int, input().split())
    dice = [0 for i in range(6)]
    for n in numbers:
        dice[n-1] += 1
    if max(dice) == 3:
        price = 10000 + (dice.index(3) + 1) * 1000
    elif max(dice) == 2:
        price = 1000 + 100 * (dice.index(2) + 1)
    elif max(dice) == 1:
        price = 100 * max(numbers)

    if max_price < price:
        max_price = price
    
print(max_price)
