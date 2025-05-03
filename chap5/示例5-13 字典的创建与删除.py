'''
字典类型的创建方式
1.使用{}直接创建字典.d={key1:value1,key2:value2......}
2.使用内置函数dict()创建字典.dict(key1=value1,key2=value2...)
字典采用哈希表，内部元素内存结构是无序的
'''

# (1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时，value值进行了覆盖

# (2)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj) # <zip object at 0x00000270D8CFFE00>
# print(list(zipobj)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoocar')]
d=dict(zipobj)
print(d) # {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# 使用参数创建字典
d=dict(cat=10,dog=20) #左侧cat是key，右侧的是value
print(d)

t=(10,20,30)
print({t:10}) # t是key,10是value，元组是可以作为字典中的key

#lst=[10,20,30]
#print({lst:10}) # TypeError: unhashable type: 'list'
# 列表是可变数据类型，字典中的键必须是不可变数据类型

# 字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))
# 字典的删除
del d
# print(d)

