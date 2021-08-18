#反转一个整数，例如-123 --> -321
class Solution(object):
    def reverse(self,x):
        if -10<x<10:
            return '输入数字过短无法翻转'
        str_x = str(x)
        if str_x[0] != '-':
            str_x = str_x[::-1]
            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648<x<2147483647 else 0

if __name__ == '__main__':
    s = Solution()
    reverse_int = s.reverse(int(input('请输入翻转数字：')))
    print(reverse_int)