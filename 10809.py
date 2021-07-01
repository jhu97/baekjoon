import sys 
import string
input = sys.stdin.readline

S = input().rstrip()

order = [-1 for _ in range(26)]
alphabets = list(string.ascii_lowercase)

for s in S:
    a = alphabets.index(s)
    order[a] = S.index(s)

print(*order, sep = ' ')
