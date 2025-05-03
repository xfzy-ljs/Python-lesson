t=(i for i in range(1,4)) # 元组生成式产生的结果是一个生成器，需要转换成元组或者列表才能查看
print(t)
#t=tuple(t)
#print(t)
# 遍历
#for item in t:
#    print(item)
print(t.__next__()) # 也起到遍历作用，但需要把前面的操作都注释掉
print(t.__next__())
print(t.__next__())

t=tuple(t)
print(t)