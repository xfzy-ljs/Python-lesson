lst1=['G1569','G1567','G8917','G203']
lst2=[['北京南-天津南','18:06','18:39','00:33'],
      ['北京南-天津南','18:15','18:49','00:34'],
      ['北京南-天津西','18:28','19:19','00:59'],
      ['北京南-天津南','18:35','19:09','00:34'],
      ]
print('车次    出发站-到达站      出发时间     到达时间      历时时长')
dict_ticket=dict(zip(lst1,lst2))

# 遍历字典中的元素
for key in dict_ticket.keys():
    print(key,end='  ') #为什么不换行，因为车次和车次的详细信息在一行显示
    # 根据key获取出来的值是一个列表
    for item in dict_ticket.get(key):
    # 根据key获取值
         print(item,end ='\t\t')
    # 换行
    print()

# 输入用户的购票车次
train=input('请输入要购买的车次：')
# 根据key获取值
info=dict_ticket.get(train,'车次不存在') # info是一个列表类型
# get(key,default=None)
#判断车次是否存在
if info!='车次不存在':
    person=input('请输入乘车人，如果是多位乘车人，请使用逗号分隔：')
    # 获取车次的出发站-到达站，还有出发时间
    s=info[0]+' '+info[1]+'开'
    print('您已购买了'+train+' '+s+'，请'+person+'尽快换取纸质车票。【铁路客服】',end='\t')
else:
    print('对不起，选择的车次可能不存在')





