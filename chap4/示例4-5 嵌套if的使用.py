answer=input("请问您喝酒了吗？请回答yes或者no\n")
if answer=='yes':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('不构成酒驾，追你一路平安')
    elif proof<80: # 20<=proof<80
        print('已构成酒驾，请不要开车')
    else: # 80<=proof
        print('已达到醉驾标准，千万不要开车')
else:
    print('哪凉快哪呆着去')