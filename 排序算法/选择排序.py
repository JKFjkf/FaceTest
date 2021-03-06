#选择排序是另一个很容易理解和实现的简单排序算法。学习它之前首先要知道它的两个很鲜明的特点。
#1. 运行时间和输入无关
#为了找出最小的元素而扫描一遍数组并不能为下一遍扫描提供任何实质性帮助的信息。因此使用这种排序的我们会惊讶的发现，一个已经有序的数组或者数组内元素全部相等的数组和一个元素随机排列的数组所用的排序时间竟然一样长！而其他算法会更善于利用输入的初始状态，选择排序则不然。
#2. 数据移动是最少的
#选择排序的交换次数和数组大小关系是线性关系，选择排序无疑是最简单直观的排序。看下面的原理时可以很容易明白这一点。

def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if ary[j] < ary[min]:
                min = j
        ary[min],ary[i] = ary[i],ary[min]
        return ary


