i = int(input('회원 등급을 선택하세요. \n 1.VVIP 2.VIP 3.GOLD'))
s = int(input('SnS 발송 건수를 입력하세요.'))
m = int(input('MMS 발송 건수를 입력하세요.'))

if i == 1:

    print('smsPrice :', 0)
    if m <= 50:
        print('mmsPrice :', 0)
    else :
        print('mmsPrice :', m * 20)

if i == 2:
    if s <= 100:
        print('smsPrice :', 0)
    else :
        print('smsPrice :', s * 10)
    if m <= 10:
        print('mmsPrice :', 0)
    else :
        print('mmsPrice :', m * 20)

if i == 3: 
    if s <= 10:
        print('smsPrice :', 0)
    else :
        print('smsPrice :', s * 10)
    if m <= 5:
        print('mmsPrice :', 0)
    else :
        print('mmsPrice :', m * 20)

