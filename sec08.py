""" 클래스 """
# class 클래스명:

class empty:
    pass            # 코드 실행에 영향을 끼치지 않게 하는 명령어

class UserInfo:
    def __init__(self, name):
        self.name=name
        print('Name:', self.name)
user1=UserInfo('kang')
user2=UserInfo('Park')
print(id(user1))
print(id(user2))
print('user1:',user1.__dict__)
print('user2:',user2.__dict__)