#使用基类
#New 是真正创建实例对象的方法，所以重写基类的new 方法，以此保证创建对象的时候只生成一个实例
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