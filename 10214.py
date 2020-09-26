T = int(input())
for _ in range(T):
    Yonsei = 0
    Korea = 0
    for i in range(9):
        Y, K = map(int,input().split())
        if Y > K:
            Yonsei += 1
        elif K > Y:
            Korea += 1
        else:
            pass
    if Yonsei > Korea:
        print('Yonsei')
    elif Korea > Yonsei:
        print('Korea')
    else:
        print('Draw')
