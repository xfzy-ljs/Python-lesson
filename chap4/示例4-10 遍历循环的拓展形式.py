s=0 # 用于存储累加和
for i in range(1,11):
    s+=i
else: # 只有前方语句块正常执行完毕才执行else部分
    print('1-10之间的累加和为：',s)
