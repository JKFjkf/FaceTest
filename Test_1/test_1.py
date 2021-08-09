def get_line():
    with open("file.txt",'rb') as f:
        return f.readline()
if __name__ == '__main__':
    for e in get_line():
        process(e)
#现在要处理一个大小为10G的文件，但是内存只有4G，如果在只修改get_lines 函数而其他代码保持不
#变的情况下，应该如何实现？需要考虑的问题都有那些？

def get_line():
    with open('file.txt','rb') as f :
        for i in f :
            yield i

def get_lines():
    l = []
    with open('file.txt','rb') as f:
        data = f.readlines(60000)
        l.append(data)
        yield l