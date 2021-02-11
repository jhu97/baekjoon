def solve(a):
    b = [0 for _ in range(1000001)]
    for i in a:
        b[i] += 1
    total = 0
    for idx, val in enumerate(b):
        total += idx * val
    return total
