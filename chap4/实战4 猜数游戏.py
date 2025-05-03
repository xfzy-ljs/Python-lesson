import random
rand=random.randint(1,100)
count=1 # 用于猜数次数
while count<=10:
    x=eval(input("在我心中有个数，1~100之间，请你猜一猜:"))
    if x<rand:
        print("小了")
        count+=1
    elif x>rand:
        print("大了")
        count += 1
    else:
        print('恭喜你猜对了！')
        break
print('您一共猜了',count,'次',sep='')


