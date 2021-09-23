def bubble_sort(ary):
    n = len(ary)
    for i in range(n):
        for j in range(1,n-i):
            if ary[j-1] > ary[j]:
                ary[j-1],ary[j] = ary[j],ary[j-1]
    return ary

#优化:某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可
def bubble_sort(ary):
    n = len(ary)
    for i in range(n):
        flag = True
        for j in range(1,n-i):
            if ary[j] < ary[j-1]:
                ary[j],ary[j-1] = ary[j-1],ary[j]
                flag  = False

        if flag:
            break
    return ary