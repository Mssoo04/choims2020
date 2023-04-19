for i in range(1, 541):
    if i % 10 == 0 and i % 25 == 0:
        print(9 + i // 60,'시', i % 60, '분')
    elif i % 25 == 0 and i % 30 == 0:
        print(9 + i // 60,'시', i % 60, '분')
    elif i % 10 == 0 and i % 30 == 0:
        print(9 + i // 60,'시', i % 60, '분')
