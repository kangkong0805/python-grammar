import this
import sys
print()
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print()

print("My Name is kangkong")

myname='kangkong'
if myname == 'kangkong':
    print("hello")

for i in range(1,10):
    for j in range(1,10):
        print('%d * %d =' %(i,j),i*j)

이름 = "강경민"   # 한국어 변수 선언 가능
print(이름)

def 인사():       # 한국어 함수 선언 가능
    print("안녕하세요, 반갑습니다.")
인사()

class Cookie:
    pass

cookie = Cookie()
print(id(cookie))
print(dir(cookie))

