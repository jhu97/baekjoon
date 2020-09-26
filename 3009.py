x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())
X = []
Y = []
X.extend((x_1, x_2, x_3))
Y.extend((y_1, y_2, y_3))
X.sort()
Y.sort()
x_4, y_4 = 0, 0
if X[0] == X[1]:
    x_4 = X[2]
elif X[1] == X[2]:
    x_4 = X[0]
if Y[0] == Y[1]:
    y_4 = Y[2]
elif Y[1] == Y[2]:
    y_4 = Y[0]
print(x_4, y_4)
