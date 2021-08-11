#第三种方法：元类，元类是用于创建类对象的类，类对象创建实例对象时一定要调用call方法，因此在
#调用call时候保证始终只创建一个实例即可，type是python的元类
class sibgleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls,'__instance'):
            cls.__instance = super(sibgleton,cls).__call__(*args,**kwargs)
        return cls.__instance

class Foo(metaclass=sibgleton):
    pass

foo_1 = Foo()
foo_2 = Foo()
print(foo_1 is foo_2)