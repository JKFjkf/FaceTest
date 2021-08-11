#创建单例时，只执行1次__init__方法
#实例化一个单例
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance
    def __init__(self,age,name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe")

print(id(a))
print(id(b))


print(a.age)
print(b.age)

a.age = 19
print(b.age)