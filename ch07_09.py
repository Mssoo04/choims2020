#가로 2배, 세로 3배 증가 / 삼각형 넓이 < 150
r = 2
h = 3

while h * r / 2 < 150:
    print('넓이', h * r / 2)
    r += 2
    h += 3
    if h * r / 2 >= 150: break
