__author__ = 'teacher'

import re

print('a\nb')
print(r'c\nd')          # raw string : escape 문자들이 무시됨, 문자로써 처리함

# re모듈의 match() 함수 : 문자열이 시작부터 일치하는지는 검사한다.
# 문자열이 매칭된 경우 Match 객체를 반환하고, 매칭되지 않은 경우 None을 반환한다.
print(re.match('[0-9]', '1234'))

# 매칭된 문자열은 Match 객체의 group() 메소드를 사용해서 추출한다.
m = re.match('\d', '1234')
print(m.group())

# +: 1회 이상 반복
print(re.match('\d+', '1234').group())

# * : 0회 이상 반복, \s : 공백문자
print(re.match('\s*\d+', '  1234 ').group())

# re모듈의 search() 함수는 부분적으로 일치하는 문자열이 있는지 검사한다.
print(re.search('\d+', ' 1234 ').group())
print(re.search('\d+', ' -1234abc ').group())

# sub : search & replace
# . : any character
# ? : 앞의 문자가 없거나 있거나 ex) ab? -> a 또는 ab

s = "<h1>title</h1>"
print(re.sub('<.*>', '', s))    # 가능한 부분을 최대로 찾음
print(re.sub('<.*?>', '', s))   # 가능한 부분을 최소로 찾음
s = "<body>Click <a href='http://www.python.org/'>Here</a></body>"
print(re.sub('<.*?>', '', s))

# URL로 지정된 웹 문서를 가져와서 모든 태그를 제거하고 텍스트만 출력해보자.
import urllib.request
s = urllib.request.urlopen('https://en.wikipedia.org/wiki/Korea').read()
print(type(s), s)

# decode() : bytes 타입을 문자열로 바꾸기
# flags=re.DOTALL : .에 newline도 포함시켜 없애기
s = re.sub('<.*?>', '', s.decode(), flags=re.DOTALL)

# 소문자로
s = s.lower()

# 알파벳과 space를 제외한 모든 문자 제거
s = re.sub('[^a-z\s]', '', s)

ws = s.split()
# print(ws)

import collections
c = collections.Counter(ws)

# print(c.items())
print(c.most_common(5))