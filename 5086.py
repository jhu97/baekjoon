while True:
    try:
        a, b = map(int, input().split())
        if b % a == 0:
            print('factor')
        if a % b == 0:
            print('multiple')
        if a % b != 0 and b % a != 0:
            print('neither')
    except ZeroDivisionError:
        break
