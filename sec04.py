# 리스트: 순서 있음, 중복 가능, 수정 가능, 삭제 가능

""" 리스트 선언 방법 """
a=[]
b=list()
c=[1,2,3,4]
d=[1,100,'Pen','Cap','Plate']
e=[1,100,['Pen','Cap','Plate']]

''' 인덱싱 '''
print(d[3])
print(d[-1])                # 인덱스 번호가 음수일 경우 역순행적으로 처리
print(d[0]+d[1])    
print(d[3]+d[4])
print(e[2][1])
print(e[-1][-3])

''' 슬라이싱 '''
print('===='*20)            # 해당 문자열 20번 출력
print(d[0:3])               # 0번째 인덱스부터 2번째 인덱스까지 출력
print(d[:3])                # 인덱스 처음부터 2번째 인덱스 까지 출력
print(d[2:])                # 2번째 인덱스부터 인덱스 끝까지 출력
print(e[2][0:2])            # 2번째 인덱스에서 0번째 인덱스부터 1번째 인덱스까지 출력
print(c+d)
print(c*3)
print('bol'+d[2])
print('PI'+str(c[c[c[0]]])) # 자료형을 맞추어준다.

print('===='*20)
c[0]=5
print(c)
c[1:2]=['a','b','c']        # 리스트 c의 1번째 인덱스부터 2번째 인덱스 전까지 리스트 값을 추가
print(c)
c[1]=['a','b','c']          # 리스트 c의 1번째 인덱스에 리스트를 추가
print(c)
c[1:3]=[]
print(c)
del c[3]                    # 리스트 c의 3번째 인덱스를 삭제
print(c)
c[0:3]=[1,2,3,4]
print(c)
c[0:4]=[2,5,3,8,4,9,1,10,6]
print(c)

c.append(0)         # 리스트 c의 인덱스 하나를 더 만들어 0을 추가
print(c)
c.sort()            # 리스트 c를 오름차순으로 정렬
print(c)
c.reverse()         # 리스트 c를 내림차순으로 정렬
print(c)
c.insert(0,11)      # 리스트 c의 0번째 인덱스에 11을 추가
print(c)
c.remove(1)         # 리스트 c에 있는 값 1을 삭제
print(c)
c.pop()             # 리스트 c의 있는 마지막 인덱스를 삭제
print(c)
c.pop(1)            # 리스트 c의 1번째 인덱스를 삭제
print(c)
print(c.count(8))   # 해당 값의 개수 출력
ex=[10, 11]
c.append(ex)        # 해당 리스트 추가
print(c)
c.extend(ex)        # 해당 값 추가
print(c)


# 튜플: 수정 가능, 삭제 불가능

""" 튜플 선언 방법 """
a_=()
b_=(1,)
c_=(1,2,3,4)
d_=(10,100,'Banana','Pineapple','Apple')
e_=(10,100,('Banana','Pineapple','Apple'))

''' 인덱싱 '''
print(d[1])
print(d[0]+d[1]+d[1])

''' 슬라이싱 '''
print(d[:3])
print(type(d))
print(e[2][:2])

''' 연산 '''
print('hi'+e[2][1])
print('hi'+str(e[1]))
print(c+d)
print(c*3)


# 딕셔너리: 순서 있음, 중복 불가능, 수정 가능, 삭제 가능

""" 딕셔너리 선언 방법 """
a={'name':'Kim','phone':'01012345678','birth':'900204'}
b={0:'Hello python!'}
c={'arr':[1,2,3,4]}
#-------------------------------------------------------------
print(type(a))
print(type(b))
print(type(c))

print(a['name'])
print(a.get('name'))
print(b[0])
print(c['arr'][2])
print(a.keys())
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))
print('name' in a)
print('addr' in a)

'''추가'''
a['address']='Gwangju'
print(a.items())
a['rank']=[1,2,3]
print(a)


# 집합(Set): 순서 있음, 중복 불가능

""" 집합 선언 방법 """
a=set()
b=set([1,2,3,4])
c=set([1,4,5,6])
d=set([1,2,'banana','pine','apple'])
#----------------------------------------
print(type(a),a)
print(type(b),b)
print(type(c),c)

t=tuple(b)
print(type(t), t)
print(t[0], t[1:3])

l=list(c)
print(type(1), 1)
print(l[0], l[1:3])

'''집합 자료형 활용'''
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

print(s1&s2)                # 교집합
print(s1.intersection(s2))  # 교집합
print(s1|s2)                # 합집합
print(s1.union(s2))         # 합집합
print(s1-s2)                # 차집합
print(s1.difference(s2))    # 차집합

s1=set([1,2,3,4])
s1.add(5)                   # 집합 s1에 원소 5를 추가
print(s1)
s1.remove(2)                # 집합 s1의 원소 2를 제거
print(s1)