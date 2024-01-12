# 입력받는 함수 : input()
num = int(input())

# 숫자를 입력받아 0이상이면 양수, 0보다 작으면 음수 출력
if num >= 0:
    print('양수입니다!')
else:
    print('음수입니다!')

if num > 0:
    print('양수입니다!')
elif num < 0:
    print('음수입니다!')
else:
    print('0입니다!')

'''
현금이 2500원 이상이거나 카드가 있으면 마카롱을 사먹고,
현금만 1000원 이상있으면 누가바를 사먹고,
그 이외는 외상!!
'''
money = 2500
is_card = False

if money >= 2500 or is_card:
    print('마카롱!!')
elif money >= 1000:
    print('누가바!!')
else:
    print('외상!!!')



