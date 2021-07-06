import sys
input = sys.stdin.readline

alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
numbers = [3,4,5,6,7,8,9,10]
cnt = 0

S = input()

for i in range(len(S)):
    for j in range(len(alphabets)):
        if S[i] in alphabets[j]:
            cnt += numbers[j]

print(cnt)
