def func1(peice): # 接收默认参数peice
    def func2(func): # 接收被装饰的函数对象
        def func3(): # 装饰器的内容，逻辑判断
            if peice == 'dog':
                print('you are dog! ',end = '')
            if peice == 'bird':
                print('you are bird! ',end ='')
            return func() # 返回一个函数调用，调用func(),即被装饰的函数dog()和bird()
        return func3
    return func2

# 执行顺序，>>> func1() > func2() > func3()的print,并返回一个func()的调用 > func() == dog()的print
@func1(peice = 'dog')
def dog():
    print('cant fly')

@func1(peice = 'bird')
def bird():
    print('can fly')

dog()
bird()
