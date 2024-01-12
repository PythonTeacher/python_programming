# 딕셔너리 : 키와 값으로 이루어진 자료형, 순서가 없음
# 리스트처럼 변경가능하다.

a = {}
b = dict()
print(type(a), type(b))

d = {'apple': 5, 'banana': 3, 'kiwi': 5}
print(d)

print(d.get('mango', 0))
# print(d['mango'])

d['tomato'] = 7

# for key in d:
for key in d.keys():
    print(key, d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

print(len(d))

del d['tomato']
print(d)

print('tomato' in d)

# 키로 가능한 것 : 문자열, 숫자, 튜플
# 키로 안되는 것 : 리스트, 사전, 집합
# d[[1, 2, 3]] = 'test'

# 1 ~ 10 사이의 홀수만 제곱하기
l = [i ** 2 for i in range(10) if i % 2]

# 딕셔너리 comprehension
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
d = {i: i ** 2 for i in range(10) if i % 2}
print(d)

# 키를 값으로, 값을 키로 바꾸는 딕셔너리를 만들어보자
# {1: 1, 9: 3, 25: 5, 49: 7, 81: 9}
d = {v: k for k, v in d.items()}
print(d)

# 순서를 유지하는 딕셔너리
from collections import OrderedDict

od = OrderedDict()

od['one'] = 1
od['two'] = 2
od['three'] = 3

print(od)

# 파일에서 데이터 읽어오기
f = open('nickname.txt', 'r', encoding='utf-8')

nicknames = {}

for line in f:
    # print(line, end='')
    fields = line.strip().split(':')
    nicknames[fields[0]] = fields[1]

f.close()
print(nicknames)

# 단어 수를 세서 사전에 저장하기
f = open('python.txt')

txt = f.read()
print(txt)

f.close()

import re

txt = re.sub('[^a-zA-Z]', ' ', txt)
print(txt)

words = txt.lower().split()

count = {}

# {'python': 3, 'a': 5 ...}
for w in words:
    # if w not in count:
    #     count[w] = 1
    # else:
    #     count[w] += 1
    count[w] = count.get(w, 0) + 1

print(count)

# 카운터 객체
from collections import Counter
c = Counter(words)

print(c)

print(c['and'])

# 빈도수가 많은 3개 단어 가져오기
print(c.most_common(3))