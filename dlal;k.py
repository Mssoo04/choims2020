#n을 입력 받은 후 1~n까지의 홀수를 출력
#합을 구하여함
i = 0
num = int(input('양의 정수를 입력하시오.'))
for a in range(1, num+1):
    if a % 2 ==1:
        print(num, '까지의 홀수는', a)
        i += a
print(num,"까지의 홀수들의 합은 :", i)
