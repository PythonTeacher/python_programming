__author__ = 'teacher'

# 모듈 : 서로 연관된 작업을 하는 코드들의 모임
# 모듈에는 함수, 클래스, 변수를 정의할 수 있다.

# 모듈의 종류 : 표준 모듈 (파이썬 제공 모듈), 사용자 생성 모듈
#              서드 파티 모듈 (외부에서 만들어서 배포하는 모듈)

import math

print(dir(math))
print(math.pi)

import mymath
print(dir(mymath))
print(mymath.pi)

# 모듈을 검색해오는 경로
import sys
print(sys.path)

# ['D:\\Python\\PyCharmProjects\\PythonClass\\24_module',
# 'C:\\Python34\\lib\\site-packages\\jinja2-2.8-py3.4.egg',
# 'C:\\Python34\\lib\\site-packages\\markupsafe-0.23-py3.4.egg',
# 'C:\\Python34\\lib\\site-packages\\google_api_python_client-1.4.1-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\uritemplate-0.6-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\six-1.9.0-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\oauth2client-1.4.12-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\httplib2-0.9.1-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\simplejson-3.8.0-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\rsa-3.2-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\pyasn1_modules-0.0.7-py3.4.egg', 'C:\\Python34\\lib\\site-packages\\pyasn1-0.1.8-py3.4.egg', 'D:\\Python\\PyCharmProjects\\PythonClass\\12_string', 'D:\\Python\\PyCharmProjects\\PythonClass\\21_tuple', 'D:\\Python\\PyCharmProjects\\PythonClass\\00_introduce', 'D:\\Python\\PyCharmProjects\\PythonClass\\14_while', 'D:\\Python\\PyCharmProjects\\PythonClass\\26_file', 'D:\\Python\\PyCharmProjects\\PythonClass\\10_number_type', 'D:\\Python\\PyCharmProjects\\PythonClass\\16_function', 'D:\\Python\\PyCharmProjects\\PythonClass\\.idea', 'D:\\Python\\PyCharmProjects\\PythonClass\\11_bool_type', 'D:\\Python\\PyCharmProjects\\PythonClass\\15_for', 'D:\\Python\\PyCharmProjects\\PythonClass\\13_if', 'D:\\Python\\PyCharmProjects\\PythonClass\\20_list', 'D:\\Python\\PyCharmProjects\\PythonClass\\22_dictionary', 'D:\\Python\\PyCharmProjects\\PythonClass', 'D:\\Python\\PyCharmProjects\\PythonClass\\25_package', 'D:\\Python\\PyCharmProjects\\PythonClass\\23_set', 'D:\\Python\\PyCharmProjects\\PythonClass\\24_module', 'C:\\windows\\SYSTEM32\\python34.zip', 'C:\\Python34\\DLLs', 'C:\\Python34\\lib', 'C:\\Python34', 'C:\\Python34\\lib\\site-packages']

# 검색 경로에 모듈을 추가하고자 하는 경우
sys.path.append('C:\\temp')

# 환경변수 PYTHONPATH에 추가

# 모듈 가져오는 방법
# 1. 일반 import : import math -> math.sqrt(25)
# 2. 함수 import : from math import sqrt -> sqrt(25)
# 3. * import : from math import *

# 함수 import
from mymath import *

print(pi)
print(my_add(10,20))

from math import pi
from mymath import pi as my_pi
from mymath import my_add

print(pi)
print(my_pi)

print(my_add.__module__)

# 모듈의 공유
# a.py -> import math, import b
# b.py -> import math, import c
# c.py -> import math

# 모듈의 reloading
import importlib
importlib.reload(math)

# 다양한 파이썬 모듈
import os

print(os.getcwd())

print(os.listdir(os.getcwd()))

# 난수구하기
import random

for i in range(10):
    print(random.randint(1, 10))
    print(random.randrange(1, 11))

# URL로 HTML 파일 가져오기
from urllib.request import urlopen

f = urlopen('http://www.python.org')

print('*' * 20, '<< header >>', '*' * 20)
print(f.headers)        # 헤더 정보

html = f.read()        # HTML 문서 읽기
print('*' * 20, '<< html >>', '*' * 20)
print(html)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())

# 웹 브라우저 열기
import webbrowser

webbrowser.open('http://www.python.org')
