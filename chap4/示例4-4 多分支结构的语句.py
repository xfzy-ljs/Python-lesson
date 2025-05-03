score=eval(input('请输入您的成绩：'))
# 多分支结构
if score<0 or score>100:
    print('成绩有误')
elif 0<=score<60:
    print('不及格')
elif 60<=score<70:
    print('及格')
elif 70<=score<80:
    print('良')
elif 80<=score<90:
    print('优')
else:
    print('名列前茅，继续保持！')
