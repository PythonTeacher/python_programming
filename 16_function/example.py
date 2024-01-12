__author__ = 'teacher'

# 함수 만들기 (기본형)
def add(a, b):
    return a + b

print(add(3, 4))
print(add(1.2, 3.4))
print(add('hello', ' world!'))

# 함수의 리턴값 여러개 리턴하기
def plus_minus(a, b):
    return a + b, a - b

x, y = plus_minus(3, 5)
print(x, y)

# 매개변수의 디폴트값 설정하기 (뒤부터 설정하기)
def add(a = 1, b = 2):
    return a + b

print(add())
print(add(5))
print(add(5, 10))

# 키워드로 매핑하기
print(add(a = 7))
print(add(b = 9))
print(add(a = 7, b = 9))

# 튜플(tuple) 간단히 알아보기
t = (1, 2, 3, 'hi', 3.14)

for i in t:
    print(i)

# 여러개를 입력받는 가변인자 함수
# args라는 이름으로 입력값들을 전부 모아서 하나의 튜플로 만듬
def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_many())
print(sum_many(10))
print(sum_many(10, 20))
print(sum_many(10, 20, 30))

# 딕셔너리 간단히 알아보기
d = {'apple':3, 'banana':2, 'kiwi':5}
for key in d:
    print(key, d[key])

# 키워드 가변인자 함수
# kwargs라는 이름으로 입력값들을 모두 모아 딕셔너리 형태로 만듬
def sum_many_keyword(**kwargs):
    sum = 0
    for key in kwargs:
        sum += kwargs[key]
    return sum

print(sum_many_keyword(a = 1, b = 2, c = 3))
print(sum_many_keyword(a = 1, b = 2, c = 3, d = 4))

'''
지난달 남은 돈 : 500원
길 가다가 주운 돈 : 100원, 200원 => 가변인자 (튜플)
아빠한테 받은 돈 : 10000원
엄마한테 받은 돈 : 5000원 => 키워드 가변인자 (딕셔너리)
현재 가진 돈은 얼마인가?
'''
def pocket_money(initial, *args, **kwargs):
    # 현재 가진 돈을 구하여 리턴하기
    sum = initial
    for i in args:
        sum += i
    for key in kwargs:
        sum += kwargs[key]
    return sum

print(pocket_money(500, 100, 200, dad=10000, mom=5000))

# 지역변수와 전역변수
# a라는 변수를 100증가시키는 함수를 만들자
a = 1           # 전역변수

def add():
    global a    # 전역변수
    a += 100    # 지역변수

add()
print(a)

# 재귀함수
# 10부터 카운트다운하여 로켓을 발사시키자
import time

def countdown(n):
    if n == 0:
        print("로켓 발사!!")
    else:
        print("count =>", n)
        time.sleep(1)       # 1초 동안 stop
        countdown(n - 1)

# countdown(10)

# 람다 함수 : 이름이 없는 함수, 한번 쓰고 버리는 용도 (로직이 간단)
# 형식) lambda 인자: 표현식  -> 표현식 결과가 리턴됨

print(lambda x: x * 2)
print((lambda x: x * 2)(3))     # 입력값이 x에 전달

# 정수 두개를 입력받아 합을 리턴하는 람다 함수 만들기
func = lambda x, y: x + y
print(func(2, 3))
print(func(10, 20))

# 입력값이 없는 람다함수
print((lambda : 'no input')())

# 리스트 간단히 알아보기
l = [1, 2, 3, 'hi', 3.14]

for i in l:
    print(i)

t = (1, 2, 3)
print(list(t))

# 람다함수 + map함수
# 형식) map(함수, 리스트)
# 리스트에 들어있는 원소들을 함수에 하나씩 적용시킨다.

# 1 ~ 5까지의 숫자의 제곱을 구하라
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))

# range(1, 6)
print(list(map(lambda x: x ** 2, range(1, 6))))

# 온도 변환하기
# 섭씨(c) -> 화씨(f) 변환 공식 (f = c * 1.8 + 32)
# 화씨(f) -> 섭씨(c) 변환 공식 (c = (f - 32) / 1.8)
celsius = [39.2, 36.5, 37.3, 37.8]

fahrenheit = list(map(lambda c: c * 1.8 + 32, celsius))
print(fahrenheit)

celsius1 = list(map(lambda f: (f - 32) / 1.8, fahrenheit))
print(celsius1)

# 각 단어의 길이를 구하여 출력해보자
sentence = 'It is raining cats and dogs'
words = sentence.split()
print(words)        # len(문자열)

print(list(map(lambda w: len(w), words)))

# 람다함수 + filter 함수
# 형식) filter(함수, 리스트)
# 리스트에 들어있는 원소를 함수에 적용시켜서 결과가 참인 것만 골라낸다.

l = [1, -3, 2, 0, -5, 6]

print(list(filter(lambda x: x > 0, l)))

# 1 ~ 10까지 숫자 중 홀수만 리턴하기
print(list(filter(lambda x: x % 2, range(1, 11))))
