#写一个列表生成式，产生一个公差为11的等差数列
for x in range(10):
    x = x*11
    print(x)

print(*(x*11 for x in range(10)))