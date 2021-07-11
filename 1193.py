import sys
import math

input = sys.stdin.readline

N = int(input())
n = math.ceil((-1 + math.sqrt(1 + 8 * N)) / 2) 
x = (n ** 2 + n) / 2

if n % 2 == 0:
    answer = '{0}/{1}'.format(int(N + n - x), int(1 + x - N))
else:
    answer = '{0}/{1}'.format(int(1 + x - N), int(N + n - x))
print(answer)

'''
import sys
import math
input = sys.stdin.readline

X = int(input())

n = math.ceil((-1 + math.sqrt(1 + 8 * X)) / 2)
rest = X - n * (n - 1) / 2
N = n + 1

if N % 2 == 0:
    print('{}/{}'.format(int(N - rest), int(rest)))
else:
    print('{}/{}'.format(int(rest), int(N - rest)))
'''
