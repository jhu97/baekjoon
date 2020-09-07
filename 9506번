while True:
    n = int(input())
    if n == -1:
        break
    sum = 0
    i_list = []
    for i in range(1, n):
        if n % i == 0:
            sum += i
            i_list.append(str(i))
    if sum == n:
        print(n, '=', ' + '.join(i_list))
    else:
        print(n, 'is NOT perfect.')
