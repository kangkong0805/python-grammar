""" 클래스 """
# class 클래스명:



class empty:
    pass            # pass: 코드 실행에 영향을 끼치지 않게 하는 명령어

class UserInfo:
    def __init__(self, name):
        self.name=name
        print('Name:', self.name)
user1=UserInfo('Kang')  # UserInfo 클래스에 'kang' 메서드를 전달
user2=UserInfo('Park') 
print(id(user1))
print(user2)
print('user1:',user1.__dict__)
print('user2:',user2.__dict__)

class Student:
    name='Student'
    age=0
    def __init__(self,name,age)->None:
        self.name=name
        self.age=age

    def __del__(self):
        print('객체삭제!')
    def info(self):
        print('My name is',self.name)
        print('I am',self.age,'years old')

s=Student('Jaehyun',22)
s.info()
del s       # del: 변수 삭제
# print(type(s))

class Student1:
    def __init__(self,name,age)->None:
        self.university='SNU'
        self.name=name
        self.age=age
        self.isStudying=True
        self.studyHour=0
    def study(self):
        if self.isStudying:
            self.studyHour+=1
    def hourstudy(self):
        print('{} 현재 공부시간: {}시간'.format(self.name, self.studyHour))