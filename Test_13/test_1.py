#求出列表所有奇数并构造新列表
a = [1,2,3,4,5,6,7,8,9,10]
res = [i for i in a if i%2==1]
print(res)