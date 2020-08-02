def factorial(n):
    """__doc__"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(10))
# <class 'function'>类的实例
print(type(factorial))
print(factorial.__doc__)
# 输出函数注释内容和
print(help(factorial))
# 一等函数，可以赋值给变量，通过变量名字调用
fact = factorial
fact(5)
# 一等函数, 作文参数传递给函数
map(factorial, range(10))
# 高阶函数 map filter reduce
from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))
# 匿名函数lambda
# callable() 判断对象是否被调用
a = [callable(obj) for obj in (abs, str, 123)]
print(a)

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        # 将列表随机排序
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingCage')

    def __call__(self):
        # 使BingoCage类像函数一样被调用
        return self.pick()


def tag(name, *content, cls=None, **attrs):
    """生成一个或者多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s=%s ' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))


# 仅支持关键字参数 b只能是关键字参数
def f(a, *, b): return a, b
