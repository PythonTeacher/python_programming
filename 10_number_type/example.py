__author__ = 'teacher'

# 숫자 자료형 : 정수형, 실수형, 복소수형

# 정수형 (int)
a = 10
print(type(a))

# id : 객체의 주소값을 얻어오는 내장함수
print(id(a), id(10))

# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
print(ord('a'), chr(65))

# 실수형(Float)
b = 3.14
print(type(b))

# 실수의 오차
print(5.4 + 1.2)
print(0.5 - 0.3)

# 숫자 연산
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)   # 몫을 리턴
print(a ** b)   # 거듭제곱
c, d = divmod(a, b)     # 몫과 나머지를 같이 리턴
print(c, d)

# 형변환
x = 36
y = -10.4
z = 1.23456789

print(float(x))
print(int(y))
print(abs(y))
print(round(z, 3))

import math
print(dir(math))
print(math.pi)

# 함수 간단히 살펴보기
def add(arg1, arg2):
    return arg1 + arg2

print(add(1, 2))
print(add(1.2, 3.4))
print(add("Hello", " World!!"))