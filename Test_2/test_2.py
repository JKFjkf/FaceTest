#设计实现遍历目录与子目录，抓取.pyc文件
import os

def get_files(dir,suffix):
    res = []
    for root,dirs,files in os.walk(dir):
        for filename in files:
            name,suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root,filename))

    print(res)

if __name__ == '__main__':
    get_files(r"C:\Users\hp\PycharmProjects\FaceTest\venv",'.pyc')