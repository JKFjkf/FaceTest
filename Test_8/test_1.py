#给定两个列表，怎么找出他们相同的元素和不同的元素？
list1 = [1,2,3]
list2 = [3,4,5]
set_1 = set(list1)
#print(set_1)
set_2 = set(list2)
print(set_1^set_2)
print(set_1&set_2)


#请写出一段python代码实现删除list里面的重复元素？
l1 = ['b','c','d','c','a','a']
l2 = list(set(l1))
print(l2)

l3 = list(set(l1))
l3.sort(key=l1.index)
print(l3)

l4 = sorted(set(l1),key=l1.index)
print(l4)

l5 = []
for i in l1:
    if not i in l5:
        l5.append(i)
print(l5)