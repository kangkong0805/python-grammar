print("Hello World")
print('Hello World')
print("""Hello World""")
print('''Hello World''')
print()
print('t','e','s','t',sep='')
print('2021','7','26',sep='-')
print('kang3530554','gmail.com',sep='@')
print()
print('','',sep='이게 되네 ㅋㅋ')
print('Welcome to', end=' ')
print('Python World',end=' ')
print('soft school')

# format 사용
print('{} and {}'.format('U','I'))              # { } 안에 들어가는 코드는 인덱스 역할
print('{1} and {0}'.format('U','I'))            # { } 안에 수를 지정하여 인덱스 번호 역할
print('{a} and {b}'.format(a="I'm",b='tired'))  # { } 안에 변수같은 것을 지정하여 format( ) 안에 변수에 해당하는 값 지정 가능

print("'you'")
print('"you"')
print('\'you\'')
print("\n\n\n test")

print("%s's favorite number is %d" %('kangkong', 1))                # 형식지정자에 해당하는 값은 %( ) 안에 입력
print("Test1: %5d, price: %4.2f" %(789,1234.5678))
print("Test1: {0:5d}, price:{1: 4.2f}" .format(789,1234.5678))
print("Test1: {a:5d}, price:{b: 4.2f}" .format(a=789,b=1234.5678))