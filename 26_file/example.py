__author__ = 'teacher'


# 파일 읽고 쓰기

s = 'Python is fun!!\n재미있는 파이썬'

# 파일 쓰기
f = open('python.txt', 'w')

f.write(s)
f.close()

# 인코딩 추가
f = open('python1.txt', 'w', encoding='utf-8')
f.write(s)
f.close()

# 파일 읽기
f = open('python.txt', 'r')
s = f.read()
print(s)
f.close()

f = open('python1.txt', encoding='utf-8')
s = f.read()
print(s)
f.close()

# with문으로 파일 입출력하기
with open('python1.txt', encoding='utf-8') as f:
    print(f.read())

l = ['짜장면\n', '짬뽕\n', '치킨\n']
s = '\n'.join(l)

with open('python2.txt', 'w', encoding='utf-8') as f:
    # f.write(s)
    f.writelines(l)

# 줄단위 읽기
# 1) 파일 객체의 반복자를 이용한다.
with open('python2.txt', encoding='utf-8') as f:
    for line in f:
        print(line, end='')

# 2) readline()
with open('python2.txt', encoding='utf-8') as f:
    line = f.readline()
    print(line, end='')

    while line:
        line = f.readline()
        print(line, end='')

# 3) readlines()
with open('python2.txt', encoding='utf-8') as f:
    l = f.readlines()
    print(l)

import json

data = {'one': 1, 'two': [21, 22, 23], 'three': (31, 32)}

# dumps : dict 데이터를 json string으로 변환 (encoding)
s = json.dumps(data)
print(s, type(s))

# json string -> dict 변환 (decoding)
j = json.loads(s)
print(j, type(j))