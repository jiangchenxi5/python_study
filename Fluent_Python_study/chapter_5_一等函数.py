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


# 函数注解
def clip(text: str, max_len: 'int > 80' = 80) -> str:
    # 再max_len前面或后面的第一个空格处截断文本
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        """
        str.rfind(str, beg=0 end=len(string)) 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
        str -- 查找的字符串
        beg -- 开始查找的位置，默认为 0
        end -- 结束查找位置，默认为字符串的长度。
        """
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()


print(clip.__defaults__)  # 定位参数和关键字参数的默认值
print(clip.__code__)
print(clip.__code__.co_varnames)  # 参数名+
print(clip.__code__.co_argcount)

from inspect import signature

sig = signature(clip)
print(sig)
print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ":", name, '=', param.default)
print("-" * 100)
# bind方法，验证参数
sig_tag = signature(tag)
my_tag = {'name': 'img', 'title': 'Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_tags = sig_tag.bind(**my_tag)
print(bound_tags)
for name, value in bound_tags.arguments.items():
    print(name, '=', value)
del my_tag['name']
# 绑定的参数不满足函数参数，会报错
try:
    bound_tags1 = sig.bind(**my_tag)
except BaseException as e:
    print(e)

# operator模块 itemgetter和attrgetter
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
]
from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
# 返回提取的值构成的元组
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))

from collections import namedtuple

latong = namedtuple('latong', 'lat long')
Metopolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metopolis(name1, cc, pop, latong(lat, long))
               for name1, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])

from operator import attrgetter

name1_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name1_lat(city))

# functools.partial 冻结参数
from operator import mul
from functools import partial

triple = partial(mul, 3)
# partial(fun, *args, **kwargs)
# 第一个参数使可调用对象， 后面跟着人一个定位参数和关键字参数
print(list(map(triple, range(1, 10))))
