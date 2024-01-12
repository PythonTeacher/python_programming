__author__ = 'teacher'

# 1부터 10까지 출력
count = 1
while count <= 10:
    print("count : %d" % count)
    if count == 4:
        break
    count += 1
else:               # else 블록은 break문에 의해서 중단되지 않은 경우에 실행
    print('정상 종료됨')

# 숫자 맞추기 게임
import random

# 0.0xx ~ 0.9xx
print(random.random())
print(random.random())
print(random.random())

# 0.xx ~ 9.xx
print(random.random() * 10)

# 0 ~ 9
print(int(random.random() * 10))

# 1 ~ 10
print(int(random.random() * 10) + 1)

random_number = int(random.random() * 10) + 1
guess_number = 0
count = 0

while True:
    guess_number = int(input("숫자를 입력하세요 : "))

    if guess_number == random_number:
        print("정답입니다!!")
        break
    else:
        count += 1
        if guess_number > random_number:
            print("%d 보다 작습니다." % guess_number)
        elif guess_number < random_number:
            print("%d 보다 큽니다." % guess_number)

        print("틀린 횟수 : %d" % count)

        if count == 3:
            print("다음 기회에~~")
            break

print("숫자 게임 종료")