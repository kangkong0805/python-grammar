'''---------------- 자료형 ----------------'''

v_str1 = "GoodGirl"                       # 문자열 타입
v_bool = True                             # 불리언(bollean) 타입
v_float = 10.01                           # 실수형 타입
v_int = 3                                 # 정수형 타입
v_str2 = "niceboy"                        
v_list = [v_str1, v_str2]                 # 리스트: 값이나 변수의 연속적으로 저장되는 형태의 자료형
v_dict = {"name":"kangkong", "age":30}    # 딕셔너리: key와 value의 값을 1대1로 대응시킨 형태의 사전적 데이터

print(v_dict['name'])                     # 'name'에 대응하는 'kangkong'을 출력
print(type(v_dict))
print(type(v_str1))
print(type(v_bool))
print(type(v_float))
print(type(v_int))
print(type(v_str2))
print(v_list)

a=5.    # 실수
b=5     # 정수
c=.5    # 실수
d=5.5   # 실수
print(type(a), type(b), type(c), type(d))

print(a)
print(int(a))           # 실수 -> 정수
print(b)            
print(float(b))         # 정수 -> 실수
print(complex(3,2j))    # 복소수 자료형
print(int(True))        # True = 1, False = 0

import math         # 수학 모듈 불러오기

print(math.ceil(5.1))   # ceil(a): a를 올림
print(math.floor(3.8))  # floor(a): a를 sofla
print(math.floor(3.8))  # floor(a): a를 sofla

str1 = "I am a man"
str2 = 'Good man'

# """(문자열)""",
str3 = """How 
    are 
        you?"""
str4 = '''Thank 
            you'''

print(str3)
print(str4)

# len(): 문자열의 길이를 구하는 함수
print(len(str1))
print(len(str2))
print(len(str3)) 
print(len(str4))

str_t1=''
print(type(str_t1), len(str_t1))

escape_str1 = "Do you have a \"big collection\""
escape_str2 = 'what\'s on TV'
escape_str3 = "what's on TV?" 
escape_str4 = 'This is "Book".'

print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

str_o1="Goodman"
str_o2="Orange"
str_o3="This is string example...wow!!! this is really string"
str_o4="kangkong"

print(str_o1 * 3)       # str_01 변수에 할당된 문자열이 3번 출력함
print(str_o1 + str_o2)
print('x' in str_o1)    # str_01 변수에 할당된 문자열에 'x'라는 문자가 들어가 있으면 'True', 없으면 'false'를 출력

print("Capitalize:", str_o1.capitalize())
print("Join str:", str_o1.join(["I'm ","!"]))
print("replace1:", str_o1.replace('Good','Nice'))   
print("replace2:", str_o3.replace('is','was', 3))   # 'is'를 'was'로 왼쪽부터 3번째까지 바꿈

print("split:", str_o4.split(' '))
print("sorted:", sorted(str_o1))                    # 아스키 코드 순서대로 정렬
print("reversed:", list(reversed(str_o2)))

first = "내 이름은 "
second = "kangkong 입니다."
string = first + second         # 문자열 변수 결합
print(string)
print('내 이름은', second)

str_s1 = 'Niceman'
print(str_s1[0:3])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])
print(str_s1[:])
print(str_s1[1:4:2])
print(str_s1[::3])
print(str_s1[::-1],'\n')

print("UPPER:", str_s1.upper())
print("lower:", str_s1.lower())