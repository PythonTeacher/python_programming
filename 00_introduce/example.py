__author__ = 'teacher'

# 한줄 주석
print('Hello, World!!')
print("Hello" + ", World!!")
print("Hello" ", World!!")
print(1, 2, 3, 4)

'''
여러줄
주석
'''

# 자동 줄바꿈 없애기
print(1, 2, end=" ")
print(3, 4)

# 변수 - 동적 타이핑
a = 10
print(a, type(a))

a = 3.14
print(a, type(a))

a = True
print(a, type(a))

a = "Hello"
print(a, type(a))

# 문자열 처리
a = "Python"
b = "is"
c = "fun!!"

result = a + " " + b + " " + c
print(result)

print(result.upper())
print(dir(str))