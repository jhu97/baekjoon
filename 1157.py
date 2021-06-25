import sys
input = sys.stdin.readline

a = list(input().rstrip().upper())
b = set(a)

def counting_alphabet(a,b):
    max_number = 0
    max_alphabet = ''
    for i in b:
        number = a.count(i)
        if max_number < number:
            max_number = number
            max_alphabet = i
        elif max_number == number:
            max_alphabet = '?'
    print(max_alphabet)

counting_alphabet(a,b)