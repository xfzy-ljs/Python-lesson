height=187.6#身高
print(height)
print(type(height))# type()查看height这个变量的数据类型

x=10
y=10.0
print('x的数据类型:',type(x))
print('y的数据类型:',type(y))

x=1.99E1413
print('科学计数法:',x,'x的数据类型:',type(x))

print(0.1+0.2)#不确定的尾数问题
print(round(0.1+0.2,1))# 0.3 保留1位小数
# round(x,y)函数，x代表数式,y代表要保留的位数