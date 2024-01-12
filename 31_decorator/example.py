__author__ = 'teacher'

# Decorator는 일종의 함수 wrapper로 함수를 인자로 받아 함수 앞 뒤로 특정 코드를 추가할 수 있다.
# Decorator에는 내부 함수를 생성하여 함수 자체를 리턴하게 한다.

# Decorator 만들기
def wrapper(func):          # Decorator는 함수 객체를 인자로 받는다.
    def decorated():        # 내부 함수 정의 시작
        print('before')     # 원 함수 실행 이전 코드
        func()              # 원 함수
        print('after')      # 원 함수 실행 이후 코드
    return decorated            # 함수 반환

def myfunc():
    print('myfunc')

new_myfunc = wrapper(myfunc)    # Decorator에 함수를 전달한다.
new_myfunc()                    # 장식된 함수를 실행한다.

# Decorator를 좀더 간단히 표현하기
@wrapper                    # wrapper 장식자를 사용함
def myfunc2():              # myfunc2 = wrapper(myfunc2)와 동일
    print('myfunc2')

myfunc2()

# 실행시간 구하기
import time

def elapsed_time(func):
    def decorated(*args, **kwargs):     # 가변인자, 키워드 가변인자
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        end = time.time()
        print("Elapsed time: %f" % (end-start))
    return decorated

@elapsed_time
def test():
     print('test')

test()

# HTML 태그를 Decorator를 이용하여 붙이기
# hello -> <b><i>hello</i></b>

def makeBold(func):
    def inner():
        return '<b>' + func() + '</b>'
    return inner

def makeItalic(func):
    def inner():
        return '<i>' + func() + '</i>'
    return inner

@makeBold
@makeItalic             # 먼저 호출
def hello():
    return "hello"

print(hello())            # <b><i>hello</i></b>