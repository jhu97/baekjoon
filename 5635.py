import sys
input = sys.stdin.readline
n = int(input())
birthday = []
name = []
for _ in range(n):
    text = list(input().split())
    if len(text[2]) == 1:
        text[2] = '0' + text[2]
    if len(text[1]) == 1:
        text[1] = '0' + text[1]
    yyyymmdd = int(text[3] + text[2] + text[1])
    name.append(text[0])
    birthday.append(yyyymmdd)
old = min(birthday)
young = max(birthday)
print(name[birthday.index(young)])
print(name[birthday.index(old)])
