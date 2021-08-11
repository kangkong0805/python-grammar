print('\n\n\n\n\n')

print(type(True))
print(type(False))


""" 조건식 """

if True:
    print("yes")
if False:
    print("no")

if False:
    print("You can't reach here")
else: 
    print("oh, you are here")


""" 관계연산자 """
''' >, <, >=, <=, ==, != '''

a,b=10,0
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# 참: "내용", [내용], (내용), {내용}
# 거짓: "", [], (), {}

city=""
if city:
    print("You are in :", city)
else:
    print("Please enter your city")

city="Gwangju"
if city:
    print("You are in :", city)
else:
    print("Please enter your city")


""" 논리연산지"""
''' and, or, not '''

a,b,c=100,60,15
print('and: ', a>b and b>c)
print('or: ', a>b and b>c)
print('not: ', not a>b)
print('not: ', not b>c)
print(not True)
print(not False)

print("ex1: ", 3+12>7+3)
print("ex2: ", 5+10*3>7+3*20)
print("ex3: ", 5+10>3 and 7+3==10)
print("ex4: ", 5+10>0 and not 7+3==10)

score1=90
score2='A'
if score1>=90 and score2=='A':
    print("합격하셨습니다.")
else:
    print("불합격하셨습니다.")

id1='user'
id2='admin'
grade='super'
if id1=='gold' or id2=='admin':
    print('관리자 로그인 성공')
if id2 == 'admin' and grade == 'super':
    print('최고 관리자 로그인 성공')

is_work=False
if not is_work:
    print("is work!!")

num=85
if num>=90:
    print('A학점입니다.')
elif num>=80:
    print('B학점입니다.')
else:
    print('c학점입니다.')

age,height=27,175
if age>=20:
    if height>=170: print("A지망 지원가능")
    elif height>=160: print("B지망 지원가능")
    else: print("지원 불가")
else: print("20세 이상 지원가능")

q=[1,2,3]
w={7,8,9,0}
e={'name':'Kim', 'city':'Gwangju', 'grade':'B'}
r=(10,12,14)
print(1 in q)                       # q의
print(6 in w)
print('name' in e)
print(12 not in r)
print('Gwangju' in e.values())