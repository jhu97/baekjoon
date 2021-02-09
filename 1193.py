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
