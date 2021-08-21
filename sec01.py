print() # 데이터를 화면에 출력하고 싶을 때 쓰는 함수

""" 문자열 출력 방법 """
print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')

print()
print('t','e','s','t',sep='')               # sep='': 출력할 데이터들 사이에 해당하는 내용을 추가
print(2021,7,26,sep='-')
print('kang3530554','gmail.com',sep='@')
print('','',sep='이게 되네 ㅋㅋ')
print()
print('Welcome to', end=' ')                # end='': 출력을 완료한 뒤의 내용을 수정 (기본값은 개행)
print('Python World',end=' ')
print('soft school')

""" format 사용 """
print('{} and {}'.format('U','I'))              # { } 안에 들어가는 코드는 인덱스 역할
print('{1} and {0}'.format('U','I'))            # { } 안에 수를 지정하여 인덱스 번호 역할
print('{a} and {b}'.format(a="I'm",b='tired'))  # { } 안에 변수같은 것을 지정하여 format( ) 안에 변수에 해당하는 값 지정 가능

print("'you'")
print('"you"')
print('\'you\'')
print("\n\n\n test")

print("%s's favorite number is %d" %('kangkong', 1))                # 형식지정자에 해당하는 값은 %( ) 안에 입력
print("Test1: %5d, price: %4.2f" %(789,1234.5678))                  # 1234.5678d에서 정수부분은 4자리 그대로 출력, 소수부분은 2번쩨 자리까지 반올림해서 출력
print("Test1: {0:5d}, price:{1: 4.2f}" .format(789,1234.5678))      # 각 인자랑 값이랑 대응
print("Test1: {a:5d}, price:{b: 4.2f}" .format(a=789,b=1234.5678))  # 인자에 이름을 지어 이름에 값을 대입