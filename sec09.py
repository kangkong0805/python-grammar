""" 클래스를 썼을 때와 안 썼을때의 차이점 """

''' 안 썼을 떄 '''
result1=0
def add(num):
    global result1
    result1 += num
    return result1
result2=0
def add2(num):
    global result2
    result2 += num
    return result2

'''썼을 때'''
class Calculator:
    def __init__(self) -> None:
        self.result=0
    def add(self,num):
        self.result+=num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(5))
print(cal1.add(7))
print(cal1.add(10))


class FourCal:
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second
    def add(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second

a = FourCal()
b = FourCal()

a.setdata(3,5)
print(a.add())  # 3+5
print(a.mul())  # 3*5

b.setdata(10,39)
print(b.add())  # 10+39
print(b.mul())  # 10*39

class MorefourCal(FourCal):
    def pow(self):
        result=self.first**self.second  # **: 제곱 연산자
        return result

a=MorefourCal(5,5)
b=FourCal(4,7)

print(a.add())
print(a.mul())
print(b.add())
print(b.mul())
print(a.pow())