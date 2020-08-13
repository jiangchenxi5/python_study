"""
# metaclass 为描述类的超类，同时可以改变子类的形态
# type除了可以查看数据类型外,还有一个特殊的能力，它也可以动态创建类。type可以将类的描述作为参数，并返回一个类。
# 一个类没有声明自己的元类，默认他的元类就是type,除了使用元类type，用户也可以通过继承type来自定义元类

自定义元类的主要目的是：

拦截类的创建
读取类的信息，可以做修改
返回新的类
"""

class Mymeta(type):

    def __init__(self, name, basec, dic):
        super().__init__(name, basec, dic)
        print('==>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print(self.yaml_tag)

    def __new__(cls, *args, **kwargs):
        print('==>Mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('==>Mymeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        return obj


class Foo(metaclass=Mymeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)


"""
==>Mymeta.__new__
Mymeta
==>Mymeta.__init__
Foo
{'__module__': '__main__', '__qualname__': 'Foo', 'yaml_tag': '!Foo', '__init__': <function Foo.__init__ at 0x03082580>, '__new__': <function Foo.__new__ at 0x03082538>}
!Foo
"""
foo = Foo('foo')
"""
在定义 class Foo() 定义时，会依次调用 MyMeta 的 __new__ 和 __init__ 方法构建 Foo 类，
然后在调用 foo = Foo() 创建类的实例对象时，才会调用 MyMeta 的 __call__ 方法来调用 
Foo 类的 __new__ 和 __init__ 方法
"""


class MyClass:
    pass


print(type(foo))
print(type(Foo))
print(type(Mymeta))
print(type(MyClass))
"""
<class '__main__.Foo'>
<class '__main__.Mymeta'>
<class 'type'>
<class 'type'>
"""