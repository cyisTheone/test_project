# 装饰器案例

def func1(func): # 外部闭包函数的参数四被装饰大的函数对象
    def func2():
        print('decorator print')
        return func() # 返回了外部函数接收的被装饰函数的调用
    return func2

# return func # 返回函数对象
# return fucn() # 返回函数的调用

@func1
def print_func():
    print('main function print')


# 被装饰的函数带参数

def deco(fun):
    def deco1(x,y):
        x += 5
        y += 5
        return fun(x, y)
    return deco1

@deco
def mysum(a, b):
    print(a+b)

mysum(1,2)
