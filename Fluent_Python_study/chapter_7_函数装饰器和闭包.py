"""
函数装饰器⽤于在源码中“标记”函数，以某种⽅式增强函数的⾏为。
装饰器特性：
1.能把被装饰的函数替换成其他函数
2.装饰器在加载模块时立即执行
"""
registy = []

"""
def register(func):
    def inner():
        print(f'running register{func}')
        registy.append(func)
        func()
    return inner
"""


def register(func):
    print(f'running register{func}')
    registy.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry - >', registy)
    f1()
    f2()
    f3()


# if __name__ == '__main__':
#     main()
# 使用装饰器优化’策略‘模式
"""
变量作用域
Python 不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量。
如果在函数中赋值时想让解释器把 b 当成全局变量，要使⽤ global 声明
"""


################闭包###########################
class Averager():
    # 计算平均值，类实现
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


def make_averager():
    # 计算平均值，函数实现  闭包
    series = []  # 局部变量

    def averager(new_value):
        # 在averager函数中，series是自由变量
        # ⾃由变量（free variable） 指未在本地作⽤域中绑定的变量
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames)  # 局部变量
print(avg.__code__.co_freevars)  # 自由变量
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)  # 保存的属性


def make_averager1():
    count = 0
    total = 0

    def averager1(new_value):
        nonlocal count, total
        """
        error:local variable 'count' referenced before assignment
        nonlocal 把变量标记为自由变量
        """
        count += 1
        total += new_value
        return total / count

    return averager1


avg1 = make_averager1()
print(avg1(11))

import time
import functools


# 装饰器练习
# 把被装饰的函数替换成新喊出，二者接受相同的参数，而且（通常）放回被装饰的函数本该返回的值
def clock(func):
    @functools.wraps(func)
    # 把func相关的属性，从func复制到clocked中__name__, __doc__
    def clocked(*args, **kwargs):
        # 支持关键字参数
        t0 = time.perf_counter()
        result = func(*args)
        elapses = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s (%s) -> %r' % (elapses, name, arg_str, result))
        return result

    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


@clock
@functools.lru_cache()  # 保存耗时的结果 避免相同参数重复计算
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# 单分派泛函数
from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br\>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.format(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'



if __name__ == '__main__':
    # print(time.perf_counter())
    # print("*" * 40, 'calling snooze (.123)')
    # print(time.perf_counter())
    # snooze(1)
    # print("*" * 40, 'calling factorial(6)')
    # print('6! = ', factorial(6))

    print(fibonacci(30))
