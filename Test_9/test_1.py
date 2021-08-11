#第一种方法:使用装饰器
def singleton(cls,*args,**kwargs):
    instance = {}
    def wrapper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(args,**kwargs)
        return instance[cls]
    return wrapper

@singleton
class Foo(metaclass=singleton):
    pass
foo_1 = Foo()
foo_2 = Foo()
print(foo_1 is foo_2)

