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
    def setdata(self,first,second) -> None:
        self.first=first
        self.second=second
    def add(self):
        return self.first+self.second
    def mul(self):
        return self.first*self.second

a = FourCal()
b = FourCal()

a.setdata(3,5)
print(a.add())
print(a.mul())

b.setdata(10,39)
print(b.add())
print(b.mul())