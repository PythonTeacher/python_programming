__author__ = 'teacher'

# 리스트 : 순서(시퀀스)를 가지는 객체들의 집합, 변경이 가능함
# 인덱싱, 슬라이싱이 가능

a = []
b = list()
print(type(a), type(b))

a = [1, 2, "Great"]

# 인덱싱
print(a[0], a[2], a[-1])

# 값 순차 출력
for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

for i, data in enumerate(a):
    print(i, data)

# 슬라이싱
# 2, 3번째 데이터 출력
print(a[1:3], a[1:], a[-2:])

# 리스트 뒤집기
print(a[::-1])

# 반복하기
print(a * 2)

# 연결하기
print(a + [3, 4, 5])

print(a)

# 멤버 검사
print(4 in a)

l = ["c", "java", "c++", "python"]

print("python" in l)
print("ruby" in l)

# c를 포함하고 있는 모든 문자열을 출력해보자
for word in l:
    if 'c' in word:
        print(word)

# 멤버값 변경
l[2] = "php"
print(l)

l[0:2] = ['html', 'css']
print(l)

l = ["apple", "banana", "kiwi"]

# 리스트에 있는 값을 하나의 문자열로 리턴
print(' '.join(l))

# python 내장함수
l = [1, 2, 3, 4, 5]
print(sum(l))
print(max(l))
print(min(l))

# 중첩리스트
s = [1, 2, 3]
t = ['start', s, 'end']
print(t)

# 2 출력하기
print(t[1][1])

# 삼중리스트
l = [1, ['a', ['x', 'y'], 'b'], 2]

# x 출력하기
print(l[1][1][0])

# 리스트에서 제공하는 메소드
s = [1, 2, 3]

print(dir(s))

s.append(4)
print(s)

s.insert(3, 1)      # 3 위치에 1을 추가
print(s)

print(s.index(3))   # 3이라는 값의 인덱스 리턴

print(s.count(1))

s.sort()
print(s)

s.reverse()
print(s)

s.remove(1)
print(s)

# 리스트를 스택으로 사용하기 (LIFO)
s = [1, 2, 3]

s.append(4)
s.append(5)

# pop(인덱스) : 리스트에서 해당 인덱스의 요소를 꺼내어 리턴함
# 인덱스를 생략하면 마지막 요소를 꺼내어 리턴함

print(s.pop())
print(s.pop())

while s:
    print(s.pop())

print(s)

# 큐를 리스트로 구현하기 (FIFO)
s = [1, 2, 3]

s.append(4)
s.append(5)

while s:
    print(s.pop(0))

l = [1, 2, 3, 5, 6, 9]

def my_any(l):
    for i in l:
        if i > 8:
            return True
    return False

print(any(i > 8 for i in l))

# 0보다 크고 10보다 작으면 True, 그렇지 않으면 False
def my_all(l):
    for i in l:
        if not 0 < i < 10:
            return False
    return True

print(all(0 < i < 10 for i in l))

# 1~10 사이의 숫자를 거듭제곱한 결과를 갖는 리스트를 만들어보자
data = []
for i in range(1, 11):
    data.append(i ** 2)

print(data)

# 람다 함수로 만들어보기
print(list(map(lambda x: x ** 2, range(1, 11))))

# List comprehension (C모듈로 되어 있어서 속도가 빠름)
# -> 리스트에서 정해진 규칙에 의해 새로운 리스트를 만들어냄
# 형식) 출력식 for문 <시퀀스객체> (if문)

l = [i ** 2 for i in range(1, 11)]
print(l)

# 1~10 사이의 홀수만 제곱하기 (filter -> map)
print(list(map(lambda x: x ** 2, list(filter(lambda x: x % 2, range(1, 11))))))

l = [i ** 2 for i in range(1, 11) if i % 2]
print(l)

# "apple"에서 자음만 뽑아서 출력하기
l = [c for c in 'apple' if c not in 'aeiou']
print(''.join(l))

# 2개의 시퀀스 자료형의 경우의 수 만들기
a = 'abc'
b = [1, 2, 3, 4]
l = [[x, y] for x in a for y in b]

print(l)

# 10보다 작은 3 또는 5의 배수는 3, 5, 6, 9이며, 합은 23이다.
# 1000보다 작은 3 또는 5의 배수의 합을 구해보자
# sum(list)

print(sum([x for x in range(1, 1000) if not x % 3 or not x % 5]))