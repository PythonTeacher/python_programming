# 튜플 : 순서를 가지는 자료형, 변경이 불가함
# 인덱싱, 슬라이싱이 가능함

a = ()
b = tuple()

print(type(a), type(b))

t = (1, 2, 3)

for i in t:
    print(i)

print(t[0])

print(t[1:3])

# list -> tuple
l = [1, 2, 3]
t = tuple(l)
print(t)

# tuple -> list
l = list(t)
print(l)

# 괄호는 생략 가능
t = 1, 2, 3

t = 1,
print(t)

print(t * 10)

print(t + (4, 5))

print(1 in t)

print(len(t))

# 튜플은 값을 변경할 수 없다!!!
# t[0] = 100

t = ('c', 'java', 'python', 'c')

# 튜플에 담긴 모든 값을 문자열로 변환하기
print(' '.join(t))

print(t.count('c'))

x, y, z = 10, 20, 30

# 튜플을 이용해서 swap하기
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)

a, b = 10, 20
a, b = b, a
print(a, b)

print("%d %f %s" % (10, 3.14, 'hello'))

def sum_mul(x, y):
    return x + y, x * y

r1, r2 = sum_mul(10, 20)

# 가변인자 함수
def sum_all(*args):
    print(type(args), args)
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
print(sum_all(1, 2, 3))

# packing
t = (1, 2, 'hello')

# unpacking
x, y, z = t

# 확장된 unpacking
x, *y = t
print(x, y)

*x, y = t
print(x, y)

from urllib.parse import urlparse, urlunparse

url = 'http://dimigo.in/login.php?key1=value1&key2=value2'

p = urlparse(url)   # URL을 성분별로 분해해서 튜플로 반환
print(p)
print(p.netloc)
print(p.path)
print(p.query)

# 파일명을 login2.php로 변경해보자
l = list(p)
l[2] = 'login2.php'

u = urlunparse(l)       # URL 성분들을 하나의 URL로 변환한다
print(u)








