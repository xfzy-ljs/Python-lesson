# 建议循环嵌套不要超过3层

# 输出长方形
for x in range(1,11): # 外层循环，行
    for y in range(1,11): # 内层循环，列
        if x==1 or x==10:
            print("—",end='')
        else:
            if y==1 or y==10:
                print("|",end='')
            else:
                print(' ',end='')
    print() # 作用是换行
print('-'*30)
# 输出正直角三角形
for i in range(1,6):
    # *的个数与行相同,range(1,2)，第二行，range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print()
print('-'*30)

# 输出倒直角三角形
for i in range(1,6):
   # 与上述同理，取反即可
    for j in range(0,6-i):
        print('*',end='')
    print()
print('-'*30)

# 输出等腰三角形
row=eval(input("请输入等腰三角形的行数："))
for i in range(1,row+1):
    # 打印倒三角形
    for x in range(1,row-i+1):
        print(' ',end='')
    # 打印1,3,5,7....等腰三角形range(1,2),range(1,4),range(1,6),range(1,8).......
    for y in range(1,i*2):
        print('*',end='')
    print()
print('-'*30)

# 输出菱形
row=eval(input("请输入菱形的行数："))
top_row=(row+1)//2 #上半部分行数
down_row=row-top_row #下半部分行数
if row%2==1:
    # 打印倒三角形
    for i in range(1, top_row+1):
        for x in range(1, top_row-i+1):
            print(' ', end='')
        for y in range(1, i*2):
            print('*', end='')
        print()
# 下半部分
    for i in range(1,down_row+1):
    # 打印直角三角形
        for j in range(1,i+1):
            print(' ',end='')
        for k in range(1,row-i*2+1): # 下半部分第一行少2个*，第二行少4个*.......
            print('*',end='')
        print()
    print('-'*30)
else:
    print('偶数行无法输出菱形！请重新输入：')
    row = eval(input("请输入菱形的行数："))

# 打印空心菱形
row=eval(input("请输入菱形的行数："))
top_row=(row+1)//2 # 上半部分行数
down_row=row-top_row # 下半部分行数
if row%2==1:
    # 打印倒三角形
    for i in range(1,top_row+1):
        for x in range(1,top_row-i+1):
            print(' ', end='')
        for y in range(1,i*2):
            if y==1 or y==i*2-1: # 镂空菱形，只需在菱形基础上更改打印*的判断条件即可
                print('*', end='')
            else:
                print(' ',end='')
        print()
    # 下半部分
    for i in range(1,down_row+1):
        # 打印直角三角形
        for j in range(1,i+1):
            print(' ',end='')
        for k in range(1,row-i*2+1):  # 下半部分第一行少2个*，第二行少4个*.......
            if k==1 or k==row-i*2: # 镂空菱形，只需在菱形基础上更改打印*的判断条件即可
                print('*',end='')
            else:
                print(' ',end='')
        print()
    print('-'*30)
else:
    print('偶数行无法输出菱形！请重新输入：')
    row = eval(input("请输入菱形的行数："))



