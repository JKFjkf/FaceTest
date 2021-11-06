#python代码实现删除一个list里面的重复元素
def listfun(a):
    a = list(set(a))
    print(a)


def listfun_1(a):
    list=[]
    for i in a :
        if i not in list:
            list.append(i)

        list.sort()
    print(list)

def listfun_2(a):
    b = {}
    b = b.fromkeys(a)
    c = list(b.keys())
    print(c)

if __name__ == '__main__':
    a = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    listfun(a)
    listfun_1(a)
    listfun_2(a)