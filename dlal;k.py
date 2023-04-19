for i in range(1, 100,1):
    if i < 10:
        print(i, end='')
        if i % 3 == 0:
            print('짝', end='')
    else:
        print(i, end='')
        if (i // 10) % 3 == 0:
            print('짝',end='')
        if ((i % 10) % 3 == 0 and (i % 10) != 0)== 0:
            print('짝', end='')

    print()
