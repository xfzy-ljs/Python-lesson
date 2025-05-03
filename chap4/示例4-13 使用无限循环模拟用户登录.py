# (1)初始化变量
i=0
while i<3: # (2)条件判断
    # (3)语句块
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码：')
    # 登录操作, if...else....
    if user_name=='ljs' and pwd=='leavesLOL':
       print('登陆成功！')
       break # 登陆成功后跳出循环
    else:
       if i<2:
           i += 1
           print('用户名或密码错误！您还有',3-i,'次机会',sep='')
       else:
            print('登录失败，已报警！')
