N = int(input())
M = int(input())
x = int(input()) # расстояние до одного из длинных
y = int(input()) # расстояние до одного из коротких

if N > M:
    if M - x < x:
        x = M - x
    #в x лежит минимум из x и M - x
    if N - y < y:
        y = N - y
    #в y лежит минимум из ...
    if x > y:
        print(y)
    else:
        print(x)
else:
    if N - x < x:
        x = N - x
    #в x лежит минимум из x и M-x
    if M - y < y:
        y = M - y
    #в y лежит минимум из ...
    if x > y:
        print(y)
    else:
        print(x)
