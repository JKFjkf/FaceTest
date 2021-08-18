a. 在python里凡是继承了object的类，都是新式类
b. Python3里只有新式类
c. Python2里面继承object的是新式类，没有写父类的是经典类
d. 经典类目前在Python里基本没有应用
e. 保持class与type的统一对新式类的实例执行a.class与type(a)的结果是一致的，对于旧式类来说就不
一样了。
f.对于多重继承的属性搜索顺序不一样新式类是采用广度优先搜索，旧式类采用深度优先搜索。