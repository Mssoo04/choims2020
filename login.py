# #암호가 틀리면 '암호를 다시 확인하세요!' 출력 and 다시 물어봄
# #5회 이상 실패 시 '로그인 실패!! 횟수 초과!!!' 메시지를 출력 후 종료
# #암호가 올바르다면 '로그인 됐습니다' 출력 후 종료
a = 'minsoo'
c = 0
while c < 5:
    psw = input('관리자 암호 입력')

    if psw == a:
        print('로그인 됐습니다.')
        break
    else :
        print('암호를 다시 확인하세요.')
        c += 1  
if c == 5:
    print('로그인 횟수 초과')
