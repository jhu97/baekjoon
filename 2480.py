-[2480번 : 주사위 세 개][https://www.acmicpc.net/problem/2480] [문제](https://www.acmicpc.net/problem/2480)

a, b, c = map(int, input().split())
numbers = []
numbers.extend((a,b,c))
numbers.sort()
if a == b == c :
    print(10000+a*1000)
elif numbers[0] != numbers[2] and (numbers[0] == numbers[1] or numbers[1] == numbers[2]):
    print(1000+100*numbers[1])
else:
    print(max(numbers)*100)

'''
numbers = [int(i) for i in input().split()]
dice = [0 for i in range(6)]
for n in numbers:
    dice[n-1] += 1
if max(dice) == 3:
    print(10000+1000*(dice.index(3)+1)) 
elif max(dice) == 2:
    print(1000+100*(dice.index(2)+1))
else:
    print(100*max(numbers))
'''
