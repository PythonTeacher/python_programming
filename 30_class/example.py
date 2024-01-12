__author__ = 'teacher'

# 모듈 vs 클래스
# 모듈 : 파일 단위로 이름공간(namespace)를 구성한다.
# 클래스 : 클래스의 이름공간과 클래스가 생성하는 인스턴스의 이름 공간을 각각 갖는다.

# 클래스 작성
class Simple:       # 클래스의 Header, class Simple(object)와 동일
    pass            # 클래스의 Body

print(Simple)

# 모든 파이썬 클래스는 object 클래스를 상속받는다.
print(Simple.__bases__)

# 클래스의 객체를 생성한다.
s1 = Simple()
s2 = Simple()

print(s1)

# 객체인지 확인하기
print(isinstance(s1, Simple))

# 클래스에 필드와 메소드 추가하기
# 일반 함수 정의와 동일하지만, 메소드의 첫번째 인수는 반드시 인스턴스 객체가 와야 한다.
class MyClass:
    def set(self, v):
        self.value = v
    def get(self):
        return self.value       # 클래스 내부에서 멤버변수나 메소드 호출 시에는 self를 이용한다.
    def add(self, v):
        self.value += v         # 멤버 참조
        get()                   # 클래스 외부, 모듈의 get() 함수를 호출
        return self.get()       # 클래스 내 메소드 호출

def get():
    print('모듈 내 get() 함수')

# 메소드 호출하기
# 1) 클래스를 이용하여 호출 (언바운드 메소드 호출)
obj = MyClass()
MyClass.set(obj, 10)
print(MyClass.get(obj))

# 2) 인스턴스 객체를 이용하여 호출 (바운드 메소드 호출)
# 자동으로 첫번째 인자 self에 인스턴스 객체 obj가 전달된다.
obj.set(20)
print(obj.get())
print(obj.add(30))

# 파이썬은 객체 생성 시 자동으로 멤버가 생성되지 않는다.
# 위의 경우 set() 메소드 호출 후에 value가 만들어짐
obj = MyClass()    # value가 아직 안 만들어졌음
# print(obj.get())

# 생성자 : 객체 생성 시 초기화를 위해 자동으로 호출되는 메소드 (__init__)
class MyClass2:
    def __init__(self):
        print('생성자 호출')
        self.value = 0
    def set(self, v):
        self.value = v
    def get(self):
        return self.value

obj2 = MyClass2()
print(obj2.get())

# 아래 멤버와 메소드를 갖는 클래스 작성해보기
# 클래스명 : Member
# 멤버 : 학번, 이름, 별명
# 메소드 : printMember()
# 생성자를 이용하여 멤버에 값 설정 후 printMember() 메소드로 출력하기
class Member:
    def __init__(self, id, name, nickname):
        self.id = id
        self.name = name
        self.nickname = nickname

    def printMember(self):
        print('학번:{}, 이름:{}, 별명:{}'.format(self.id, self.name, self.nickname))

    def __str__(self):
        return '[str]학번:{}, 이름:{}, 별명:{}'.format(self.id, self.name, self.nickname)


m1 = Member('2301', '나파이', '파이썬의대가')
m1.printMember()

m2 = Member('2401', '나자바', '자바의대가')
m2.printMember()

# __str__() 메소드 호출하기
print(m1.__str__())
print(m2)

# 클래스 멤버 (static)

class MyClass3:
    cls_member = 100        # 클래스 변수
    def __init__(self, ins_member):
        self.ins_member = ins_member
    def print(self):
        print(MyClass3.cls_member, self.ins_member)

obj = MyClass3(200)
print(obj.cls_member)
print(obj.ins_member)
obj.print()

print(MyClass3.cls_member)

# 클래스 메소드 만들기
class Calc:
    x = 1
    y = 2

    @staticmethod
    def add():
        return Calc.x + Calc.y

    @classmethod
    def add2(cls):
        return cls.x + cls.y

print(Calc.add())
print(Calc.add2())