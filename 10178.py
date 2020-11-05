import sys 
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    candy, brothers = map(int, input().split())
    number = candy // brothers
    dad = candy % brothers
    print("You get {0} piece(s) and your dad gets {1} piece(s).".format(number, dad))
