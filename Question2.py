# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for i in q1:                    # q1의 인덱스 개수만큼 반복
    if i=='가을': print(q1[i])  # 인덱스에 '가을'에 해당하는 데이터가 있으면 출력


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
for i in q2:
    if i=='사과'or q2[i]=='사과': print('사과') # i: key, q2[i]: value


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
n=int(input('-> '))
if n>=81 and n<=100: print('A학점')
elif n>60: print('B학점')
elif n>40: print('C학점')
elif n>20: print('D학점')
elif n>0: print('E학점')


# # 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a,b,c=12,6,18
if a<b: a=b
if a<c: a=c
print(a)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
n='050805-3123456'
if int(n[7])%2==1: print('남자')
else: print('여자')

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]
for i in q3:
    if i=='정': continue
    else: print(i,end=' ')
print()


# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for m in range(1,101,2): print(m,end=' ')
print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    if len(i)>=5: print(i,end='')
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
for i in q5:
    if i.islower() == True: print(i,end=' ')
print()


# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
print([i.upper() if i.islower() else i.lower() for i in q6])
