import os

print(__file__)     # 현재 파일 경로

print(os.path.dirname(__file__))       # 디렉토리명
print(os.getcwd())
print(os.path.basename(__file__))       # 파일명

# 파일의 존재여부 체크
print(os.path.exists('test.txt'))

# test.txt가 없으면 생성하고, 있으면 내용을 읽어 출력하기
if os.path.exists('test.txt'):
    with open('test.txt') as f:
        print(f.read())
else:
    with open('test.txt', 'w') as f:
        f.write('created!!!!')

# 파일 경로 만들기
# a, b, c, d.txt -> a/b/c/d.txt
print(os.path.join('a', 'b', 'c', 'd.txt'))

import glob

print(glob.glob('*'))

print(glob.glob('*[0-9]*'))

import shutil

shutil.copyfile('test.txt', 'test2.txt')

# rmtree

os.rename('test2.txt', 'test3.txt')

os.remove('test3.txt')


