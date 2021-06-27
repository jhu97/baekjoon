sen = input()
cnt = 0

change = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in change:
    sen = sen.replace(i, '0')

cnt = len(sen)

print(cnt)