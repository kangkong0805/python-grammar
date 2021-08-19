v1=1
while v1 < 11:          # v1가 11보다 작으면 반복
    print('v1:',v1)
    v1+=1

for i in range(10):     # 초기값은 i=0, i가 10보다 작으면 반복, i는 1씩 증가
    print('i is:', i)

for i in range(1,11):   # 초기값은 i=1, i가 11보다 작으면 반복, i는 1씩 증가
    print('i is:', i)

for i in range(1,10,2): # 초기값은 i=1, i가 10보다 작으면 반복, i는 2씩 증가
    print('i is:', i)    

sum1=0
for i in range(101):
    sum1+=i
print('1부터 100까지의 합:', sum1)

sum2=sum(range(1,101))                                          
print('1부터 100까지의 합:', sum2)
print('1부터 100까지 3의 배수의 합:', sum(range(1,101,3)))

a=int(input('enter 1st number: '))
b=int(input('enter 2st number: '))
print('두 수의 합:', a+b)

n=int(input('enter number: '))
i=2
for i in range(2, n):
    if(n%i==0):
        print("소수 아님")
if n<=1: print("소수 아님")
elif i>=n: print("소수")


name='Daisy'
for n in name:                                      # name의 문자 개수만큼 반복
    if n.isupper(): print(n, end='')
    else: print(n.upper(),end='')

numbers=[14,3,4,7,10,24,17,2,33,15,34,36,38]
for num in numbers:                                 # numbers의 리스트의 인덱스 개수만큼 반복
    if num==3: print('찾았다:', num); break
    else: print("not found!!:", num)

lt=['1',2,5,True,4.3,complex(4)]
for v in lt: 
    if type(v) is float: print('type:', type(v))    # v가 실수형 타입이면 실행

f=True
numbers=[14,3,4,7,10,24,17,2,33,15,34,36,38]
while f: 
    for v in numbers: 
        if v==33: print('found',v)
        f=False