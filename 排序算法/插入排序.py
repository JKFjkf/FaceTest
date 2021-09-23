#插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入

def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        key = i - 1
        mark = ary[i]
        while key >= 0 and ary[key]>ary[i]:
            ary[key+1]=ary[key]
            key -= 1
        ary[key+1] = mark
    return ary