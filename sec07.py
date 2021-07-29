""" 함수 """
# def function_name():

def hello(world):
    print("hello", world)
hello('kang')

def hello_return(world):
    val="hello "+str(world)
    return val
str = hello_return('kang')
print(str)


''' 다중리턴 '''

def func_mull_int(x):
    y1=x*10
    y2=x*100
    y3=x*1000
    return y1,y2,y3
val1,val2,val3=func_mull_int(5)
print(val1,val2,val3)
print(type(val1))

def func_mull_list(x):
    y1=x*10
    y2=x*100
    y3=x*1000
    return [y1,y2,y3]
lt=func_mull_list(5)
print(type(lt),lt)

def func_mull_dic(x):
    y1=x*10
    y2=x*100
    y3=x*1000
    return {'ret1':y1,'ret2':y2,'ret3':y3}
dic=func_mull_dic(5)
print(type(dic),dic.items())

def args_func(*args):
    print(args)
args_func('Kim')
args_func('Kim','Park','Lee')

def args_func(*args):
    for t in args:
        print(t)
args_func('Kim')
args_func('Kim','Park','Lee')

def args_func(*args):
    for i, v in enumerate(args):
        print(i, v)
args_func('Kim')
args_func('Kim','Park','Lee')

def kwargs_func(**kwargs):
    print(kwargs)
kwargs_func(name1='kang')
kwargs_func(name1='Kim',name2='Park',name3='Lee')


''' 혼합 '''

def example(arg_1,arg_2,*arg_3,**kwargs):
    print(arg_1,arg_2,arg_3,kwargs)
example(10,20,'park','kim','lee',age1=33,age2=34,age3=20)


''' 중첩 함수'''

def nested_func(num):
    def func_in_func(num):
        print('>>>',num)
    print('In func')
    func_in_func(num+100)
nested_func(20)