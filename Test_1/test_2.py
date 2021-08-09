from mmap import mmap


def get_line():
    with open('file.txt','rb') as f :
        m = mmap(f.fileno(),0)
        tmp = 0
        for i, char in enumerate(m):
            if char==b"\n":
                yield m[tmp:i+1].decode()
                tmp = i+1


if __name__ == '__main__':
    for i in get_line():
        print(i)