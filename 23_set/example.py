__author__ = 'teacher'

# 집합 : 여러 값을 순서없이 그리고 중복없이 모아놓은 자료형이다.
# 두가지 형태의 set 자료형
# 1. set : 변경 가능한 집합
# 2. frozenset : 변경 불가능한 집합

# 리스트나 튜플 : 순서가 있는 자료형, 인덱싱, 슬라이싱 가능
# set : 순서가 없는 자료형, 인덱싱, 슬라이싱 불가, 중복을 허용하지 않음
# set의 이러한 중복을 허용하지 않는 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용된다.

a = set()       # 비어있는 set 객체 생성
b = []          # 리스트
c = ()          # 튜플
d = {}          # 딕셔너리

print(type(a), type(b), type(c), type(d))

b = {1, 2, 3}
print(b)

# 튜플로부터 set 객체 만들기
t = (1, 2, 3, 1, 2, 3)
s = set(t)

# set은 중복을 허용하지 않음
print(s)

# 길이
print(len(s))

# 값 출력하기
for i in s:
    print(i)

# 멤버 검사
print(3 in s)

# set은 시퀀스를 갖지 않으므로, 인덱싱/슬라이싱 등의 작업이 불가함
#s[0] = 100

# set이 제공하는 메소드

# add() : 원소 한개 추가
s.add(4)
print(s)

# update() : 원소 여러개 추가
# s = s + {4, 5, 6}
s.update({4, 5, 6})     # s.union()과 동일하지만 update()는 원래 집합을 변경시킴
print(s)

# remove() : 원소를 제거한다. 원소가 없는 경우 에러 발생
# discard() : 원소를 제거한다. 원소가 없는 경우 그냥 통과
s.remove(3)
print(s)

s.discard(3)

# 집합 연산 (합집합, 교집합, 차집합)
a = {1, 2, 3, 4, 5, 6}
b = {4, 5, 6, 7, 8, 9}
c = {4, 10}

s = a.union(b)              # 합집합
print(s)

s = a.union(b, c)           # 인수가 두개 이상이어도 된다.
print(s)

s = a.intersection(b)       # 교집합
print(s)

s = a.intersection(b, c)    # 인수가 두개 이상이어도 된다.
print(s)

s = a.difference(b)         # 차집합
print(s)

# 집합의 포함관계
a = {1, 2, 3, 4, 5}
b = {1, 2, 3}

print(a.issuperset(b))
print(b.issubset(a))
print(a.isdisjoint(b))   # 교집합이 공집합인가?

# frozenset 만들기
fs = frozenset({1, 2, 3})

print(type(fs))

# frozenset 객체는 값을 변경하지 않는 연산만 허용한다.
# fs.add(10)     # 변경 불가

# set comprehension
# 1~10 사이 홀수들의 제곱 구하기
s = {v * v for v in range(10) if v % 2}
print(s)