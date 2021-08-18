#字符串 "123" 转换成 123 ，不使用内置api，例如 int()

#方法一： 利用 str 函数
def atoi_1(s):
    num = 0
    for v in s :
        for j in range(10):
            if v  == str(j):
                num = num*10 + j
    return num


#方法二： 利用 ord 函数
def atoi_2(s):
    num = 0
    for v in s:
        num = num *10 +ord(v) - ord('0')
    return num

#方法三: 利用 eval 函数
def atoi_3(s):
    num = 0
    for v in s:
        t = "%s * 1" % v
        n = eval(t)
        num = num * 10 + n
    return num


#方法四: 结合方法二，使用 reduce ，一行解决
#from functools import reduce
#def atoi_4(s):
#    return reduce(lambda num,v: num *10 +ord('v') - ord('0'),s,0)



if __name__ == '__main__':
    print(atoi_1('123'))
    print(atoi_2('123'))
    print(atoi_3('123'))
    print(atoi_4('123'))
