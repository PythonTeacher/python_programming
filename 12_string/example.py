__author__ = 'teacher'

# 문자열 : "", ''

print("Hi!!")
print('Hi!!')
# print("Hi!!')

print("I'll be back")
print('I\'ll be back')

s = "터미네이터는 말했다\n"
s += "\"I'll be back.\""
print(s)

s = """
터미네이터는 말했다.
"I'll be back"
"""
print(s)

# 문자열 연결
a = "I" + " am" + " your father."
print(a)

# 문자열 반복
print(a * 3)

'''
==================== (50번 반복)
문자열 연산
==================== (50번 반복)
'''

print('=' * 50)
print('문자열 연산')
print('=' * 50)

# 문자열 길이 (len() : 내장함수)
print(len(a))

# 문자열 연산 시 주의사항
print("10" + "2")

# 문자열 형변환
print(int("10") + 2)
print(float("3.14") + 10)
print(str(10) + " apples")  # 10 apples

# 문자열 포맷팅

# 1. 서식문자 사용 (%d, %f, %s)
print("I ate %d apples." % 5)
print("I ate 5 %s." % "apples")
print("I ate %d %s." % (5, "apples"))

print("%.4f" % 0.1234567)
print("%10.4f" % 0.2345678)

# 2. format() 내장함수 이용
print("키 : ", format(175.57, ".1f"))
print("재산 : ", format(1000000000, ",d"))

# 3. str 클래스의 format() 메소드 이용
s = "I ate {} apples.".format(5)
print(s)

s = "I ate {} {}.".format(5, "apples")
print(s)

# I ate 5 apples and 5 bananas.
s = "I ate {0} {1} and {0} {2}".format(5, "apples", "bananas")
print(s)

s = "I ate {number} {what}.".format(number=5, what="apples")
print(s)

s = "I ate {0} {what}.".format(5, what="bananas")

# 문자열 함수
print(dir(s))

print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())

print("father" in a)
print("f" in a)
print("s" in a)

print(a.count('a'))

# isXXX()
print("1234".isdigit())
print("asdf".isdigit())
print("asdf123".isalnum())

# 문자열 결합
print(" ".join(a))

# 공백 지우기
s = "    hello    "
print("[" + s.lstrip() + "]")
print("[" + s.rstrip() + "]")
print("[" + s.strip() + "]")

# 문자열 바꾸기
s = "I'm a superman."

print(s.replace("super", "spider"))

# 문자열 나누기
print(a.split())

# 문자열은 순서가 있다 -> indexing, slicing
print(a[0], a[2])

s = "hello"

# 제일 마지막의 문자를 출력해보자
print(s[len(s) - 1])
print(s[-1])

# slicing
print("01234567890123456789")
print(a)

# your 추출
print(a[5:9])       # [start:end-1]
print(a[5:])
print(a[::])

print(a[5:9:2])     # [start:end-1:step]

# I'm your father를 거꾸로 찍으려면?
print(a[::-1])

# 학번을 slicing해서 기수, 학년, 반, 번호로 잘라내기
s = "132301"

gisu = s[:2]
grade = s[2:3]
ban = s[3:4]
number = int(s[-2:])

print("{}기 {}학년 {}반 {}번".format(gisu, grade, ban, number))

# 문자열 내용은 변경 불가
# s[3] = "4"
print(s)

s = s[:3] + "4" + s[4:]
print(s)