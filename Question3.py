# 1. 입력한 숫자 n번만큼 *를 출력하는 함수를 작성하시오
# 함수명 starprint(n)
def starprint(n):
    print('*'*n, end='')
starprint(int(input('enter n: ')))  # 입력 값이 함수의 매개변수로 전달


# 2. 두수를 입력받아 합, 차, 곱을 저장하여 리스트로 출력하시오.
# 함수명 operator(a,b)
def operator(a,b):
    return[a+b,a-b,a*b]     # 리스트 형태로 반환
a=int(input('enter a: '))
b=int(input('enter b: '))
print(operator(a,b))


# 3. 문장을 입력받아서 각 알파벳을 대문자로 바꾸어 출력하는 함수작성.
# 함수명: wordlist(string)
def wordlist(string):
    print(string.upper())
a=(input('문장을 입력하세요: '))
wordlist(a)


# 4. 두 자연수를 입력받아 최대공약수를 리턴하는 함수, 최소공배수를 리턴하는 함수를 완성하시오.
# 함수명: 최대공약수 gcd(n,m), 최소공배수 lcm(n,m)
def gcd(n,m):
    max,value=n,0
    if m>n: max=m
    for i in range(1,max):
        if n%i==0 and m%i==0: value=i
    return value
def lcm(n,m):
    max,value=n,0
    if m>n: max=m
    i=max
    while i:
        if i%n==0 and i%m==0: return i
        i+=1
n,m=int(input('enter n: ')),int(input('enter m: '))
print('gcd:',gcd(n,m),'lcm:',lcm(n,m))


# 5 아래의 조건을 만족하면서, 100000보다 작은 자연수 중
# 3의 배수 또는 5의 배수를 모두 더한 합을 출력하는 프로그램을 작성하시오.
# 조건: 3의배수를 판정하는 함수-ismulThree(n), 
#       5의 배수를 판정하는 함수 - ismulfive(n),
#       전체코드는 15줄 내에서 완성하기
def ismulThree(n):
    if n%3==0: return True
    else: return False
def ismulfive(n):
    if n%5==0: return True
    else: return False
sum=0
for i in range(1,10000):
    if ismulThree(i) or ismulfive(i) == True: sum+=i
print(sum)