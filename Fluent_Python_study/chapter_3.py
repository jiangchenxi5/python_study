import sys
import re

WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurences = index.get(word, [])
            # occurences.append(location)
            # index[word] = occurences
            # setdefault 处理找不到的键
            index.setdefault(word, []).append(location)
#
# for word in sorted(index, key=str.upper):
#     print(word, index[word])
print(sys.argv)

# defaultdict:处理找不到健的一个选择
import collections

index1 = collections.defaultdict(list)
with open(sys.argv[0], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 如果没有word，则会创建一个空列表，赋值
            index1[word].append(location)


class StrKeyDict0(dict):
    # 注会被__getitem__调用，再找不到健的时候
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# print(d[1])
print(d.get(1, 'N/A'))


# 子类化UserDict
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return str(key)

    def __contains__(self, key):
        # UserDict中有一个data属性，是dict实例
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value


# 不可变的映射类型
from types import MappingProxyType

d = {1: 'a'}
# 映射的只读视图。无法修改
d_proxy = MappingProxyType(d)
print(d_proxy.get(1))

# 集合 set frozenset
s = {1}
print(type(s))
s.pop()
print(s)

from dis import dis
print(dis('{1}'))
print(dis('set([1])'))
# 字典 散列表
# 1.键必须时可散列的2.字典在内存上开销巨大3.键查询很快4.健的次序取决于添加次序
# 不要同时进行迭代和修改
# 集合适用于以上特点
print(sys.argv)
