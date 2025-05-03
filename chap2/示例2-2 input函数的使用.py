name=input('请输入您的姓名：')
print('我的姓名是：'+name)

num=input('请输入新的幸运数字：')
print('新的幸运数字是'+num)# 连接成功，说明num是字符串类型
num=int(num)# 使用内置函数int将num转成整数类型
print('新的幸运数字是',num)
print('新的幸运数字是',num,sep='')