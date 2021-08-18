#第一种方法:使用装饰器
def singleton(cls,*args,**kwargs):
    instances = {}
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls] = cls(args,**kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass
foo_1 = Foo()
foo_2 = Foo()
print(foo_1 is foo_2)

