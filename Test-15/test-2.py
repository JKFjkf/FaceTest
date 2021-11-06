#给列表中的字典排序：假设有如下list对象，alist=[{"name":"a","age":20},{"name":"b","age":30},
#{"name":"c","age":25}],将alist中的元素按照age从大到小排序 alist=[{"name":"a","age":20},
#"name":"b","age":30},{"name":"c","age":25}]
alist=[{"name":"a","age":20},{"name":"b","age":30},{"name":"c","age":25}]
alist_sort = sorted(alist,key=lambda e: e.__getitem__('age'),reverse=True)
print(alist_sort)

#sorted可以对所有可迭代类型进行排序，并且返回新的已排序的列表
#sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
