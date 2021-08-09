# 모듈: 함수나 변수 또는 클래스를 모아 놓은 파일
# import: 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
import sys  # sys 모듈을 불러옴


""" 출력 """
print()
print(sys.stdin.encoding)
print(sys.stdout.encoding)
print()
print("My Name is kangkong")


""" 조건문 """
myname='kangkong'
if myname == 'kangkong':
    print("hello")


""" 반복문 """
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d =' %(i,j),i*j)


이름 = "강경민"   # 한국어 변수 선언 가능
print(이름)


""" 함수 """
def 인사():       # 한국어 함수 선언 가능
    print("안녕하세요, 반갑습니다.")
인사()


""" 클래스 """
class Cookie:
    pass                # pass: 다음 코드로 넘어가는 명령어, 보통 클래스 생성 후 초기에 넣을 코드가 없을 때 쓰임
cookie = Cookie()
print(id(cookie))
print(dir(cookie))