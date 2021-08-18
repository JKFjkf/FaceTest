#设计实现遍历目录与子目录，抓取.pyc文件
from glob import iglob

def func(fp,postfix):
    for i in iglob(f'{fp}/**/*{postfix}',recursive=True):
        print(i)

if __name__ == '__main__':
    postfix = '.pyc'
    func(r'C:\Users\hp\PycharmProjects\FaceTest\venv',postfix)