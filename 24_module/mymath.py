__author__ = 'teacher'

pi = 3.14

def my_add(a, b):
    return a + b

# __name__ : 모듈의 이름을 가져오는 내장변수
# 직접 모듈을 호출한 경우 __main__이 들어옴
if __name__ == '__main__':
    print(pi)
    print(my_add(10, 20))