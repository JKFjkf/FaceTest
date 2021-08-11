#使用基类
class singleleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'__instance'):
            cls.__instance = super(singleleton,cls).__new__(cls,*args,**kwargs)
        return cls.__instance
class Foo(singleleton):
    pass
foo_3 = Foo()
foo_4 = Foo()
print(foo_3 is foo_4)