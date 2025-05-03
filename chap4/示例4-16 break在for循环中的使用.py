for i in 'hello':
    if i=='e':
        break
    print(i)
print('-'*30)
for i in range(3):
    user_name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user_name == 'ljs' and pwd == 'leavesLOL':
        print("正在登录，请稍后......")
        break
    else:
        if i < 2:
            print('用户名或密码错误，您还有', 2 - i, '次机会')
else: # for...else
    print('三次均输入错误！')
