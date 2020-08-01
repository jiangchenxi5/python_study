# 学列构成的数组
# 可变序列 不可变序列
# 列表推导式

print(ord('a'))
print(chr(99))
symbols = '#$%^&*@#￥%……&*'
beyond_ascii = [ord(x) for x in symbols if ord(x) > 127]
print(beyond_ascii)
beyond_ascii_filter = list(filter(lambda x: x > 127, map(ord, symbols)))
print(beyond_ascii_filter)
# 生成器表达式
colors = ['bloack', 'white']
sizes = ['S', 'M', 'L']
shirts = ('%s %s' % (c, s) for c in colors for s in sizes)
print(shirts)
for shirt in shirts:
    print(shirt)

# 元组拆包 *
# 具名元组
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')
toyko = City('Tokyo', 'JP', 36.933, (35.689722, 138.691667))
print(toyko)
# _fields创建一个包含字段名称的元组
print(City._fields)
# _make(iterable)
Beijing = ('BEIJING', 'BJ', 72.555, (34.5555, 144.4457))
beijing = City._make(Beijing)
print(beijing)
print(beijing._asdict())
# 切片
# 切片赋值
board1 = [['_'] * 3 for i in range(3)]
board1[1][2] = 'X'
print(board1)
board2 = [['_'] * 3] * 3
board2[1][1] = 'X'
print(board2)
row = ['_'] * 3
board3 = []
for i in range(3):
    board3.append(row)
board3[2][1] = 'X'
print(board3)

import sys
import bisect

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        positon = bisect_fn(HAYSTACK, needle)
        offect = positon * ' | '
        print(ROW_FMT.format(needle, positon, offect))


if sys.argv[-1] == 'left':
    bisect_fn = bisect.bisect_left()
else:
    bisect_fn = bisect.bisect
print('DEMO:', bisect_fn.__name__)
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)

# bisect.insort插入元素，保持有序列的顺序
# 数组 array如果只包含数字的列表，更高效
# 队列
