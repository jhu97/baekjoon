N = int(input())
for _ in range(N):
    text = input()
    L = len(text)
    number = 0 
    sum = 0
    for l in range(L):
        if text[l] == 'O':
            number += 1
            sum += number
        else:
            number = 0
    print(sum)
