T = int(input())
if T // 300 != 0:
    A = T // 300
    B = (T % 300) // 60
    C = ((T % 300) % 60) // 10 
    if ((T % 300) % 60) % 10 != 0:
        print(-1)
    else:
        print(A, B, C)
    
else:
    A = 0
    B = T // 60
    C = (T % 60) // 10
    if (T % 60) % 10 != 0:
        print(-1)
    else:
        print(A, B, C)
