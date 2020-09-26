text = input()
N = len(text)
answer = []

if N % 2 == 1:
    for n in range(int((N - 1)/2)):
        if text[n] == text[N - 1 - n]:
            answer.append(1)
        else:
           break
    if len(answer) == int((N - 1)/2):
        print(1)
    else:
        print(0)
else:
    for i in range(int(N/2)):
        if text[i] == text[N - 1 - i]:
            answer.append(1)
        else:
            break
    if len(answer) == int(N/2):
        print(1)
    else:
        print(0) 
