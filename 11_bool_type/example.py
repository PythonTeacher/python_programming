__author__ = 'teacher'

# bool 타입 : True 또는 False

a = 1

print(a < 0)
print(a > 0)
print(a == 0)
print(a != 0)

print("abcd" > "abb")

# bool() : bool값을 리턴하는 내장함수
print(bool(3))
print(bool(0))
print(bool("hello"))
print(bool(""))     # 값이 비어있으면 False

# 논리 연산 (and, or, not)
print(True and True)
print(True and False)

print(True or False)
print(False or False)

print(not True)

# Short-circuit 테스트
a = 10
b = 0

# print(a / b)

if True or (a / b):
    print("short-circuit yes!!!")
else:
    print("short-circuit no!!!")