lst=['hello','world','python']
print('原列表:',lst,id(lst)) # id() 查询内存地址

# 增加元素的操作
lst.append('sql')
print('增加元素之后:',lst,id(lst))
# 列表为可变数据类型，元素个数可变，但内存地址不变

# 使用insert(index,x)在指定的index位置上插入元素x
lst.insert(1,100)
print(lst)

#列表元素的删除操作
lst .remove('world')
# print(lst .remove('world')) 返回None
print('删除元素之后的列表:',lst,id(lst))

#使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

#清除列表中所有的元系clear)
#lst.clear()
#print(lst,id(lst)) # 尽管列表元素全部被删除，但内存地址依然不变

# 列表的拷贝，将产生一个新的外表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst)) # lst.copy将产生一个内存地址不同的新列表

#列表元系的修改操作
# #根据索引进行修改元系
lst[1]='mysql'
print(lst)
print('-'*50)
#列表的排序
'''
1.列表对象的sort方法，lst.sort(key=None,reverse=False)
key为排序的规则，reverse表示排序方式（升序(默认)、降序），False为升序 True为降序

2.内置函数sorted()，sorted(iterable,key=None,reverse=False)
iterable表示排序的对象
'''

lst=[4,56,3,78,40,56,89]
print('原列表:',lst,id(lst))

# 排序，默认是升序
lst.sort() # 排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序',lst,id(lst))


#排序，降序
lst.sort(reverse=True)
print('降序:',lst,id(lst))

print('-'*50)
lst2=['banana','apple','Cat','Orange','Cave','bill']
print('原列表:',lst2)
#升序排序、先排大写，再排小写。 因为ASCII码中，大写字母排在小写字母前
lst2.sort()
print('升序:',lst2)

# 降序，先排小写，后排大写
lst2.sort(reverse=True)
print('降序:',lst2)

# 忽略大小写进行比较
lst2.sort(key=str.lower) # str.lower表示按小写字母排
print(lst2)
print('-'*50)

lst=[4,56,3,78,40,56,89]
print('原列表:',lst,id(lst))

# 排序
asc_lst=sorted(lst) # 默认升序
print('升序:',asc_lst,id(asc_lst))
print('原列表:',lst,id(lst))

# 降序
desc_lst=sorted(lst,reverse=True) # sorted()会产生新的列表对象
print('降序:',desc_lst,id(desc_lst))
print('原列表:',lst,id(lst))
print('-'*50)

lst2=['banana','apple','Cat','Orange','Cave','bill']
print('原列表:',lst2)
# 忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表:',lst2)
print('排序后的列表:',new_lst2)