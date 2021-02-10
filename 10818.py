import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))

biggest = max(numbers)
smallest = min(numbers)

print(smallest, biggest)
