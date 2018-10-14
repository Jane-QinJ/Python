dict ={
	'Hello':'Hello',
	'Nice to meet you':'Nice to meet you',
	'Which fruit do you like best':'I like apple very much',
	'How old are you':'20 years old',
	'You are handsome':'Thank you'
}
#t--train 训练机器人对话；c--chat 同机器人聊天； l--leave 让机器人离开
flag='c' #让机器人默认是聊天状态
work = True #让机器人默认是工作的
print('Hi, my name is Python')
print('Do you want chat with me?')
while flag == 'c' or 't':        #聊天或训练状态时循环执行
    flag=input('你可以选择跟我聊天(c)还是训练我对话(t),或让我离开(l)?(c/t/l)')
#训练状态时
    if flag == 't':
        question = input('请输入问题(key): ')  #获取输入作为key
        answer = input('请输入回答(value):')   #获取输入作为value
        dict[str(question)] = str(answer)     #向字典中存入键值对
        print('训练成功')
        print('现在我已经会%d个问题了！'%len(dict))
        continue 			    #跳出本次循环
#聊天状态时
    elif flag=='c':
        if len(dict) == 0:			#如果字典为空
            print("我现在还不会任何问题，请先训练我！")
            continue
#获取输入作为要查找的key
        chat_word = input("谢谢你跟我聊天，你想对我说点什么？：  ")
#遍历整个字典
        for key in sorted(dict.keys()):
            if str(chat_word) == key:	#如果有相同的key
                work = True
                print(dict[key])	            #打印出对应的value
                break
            else:
                work = False			#无相同key，机器人不工作
#如果机器人为不工作状态，打印提示信息，并充值工作状态为True
        if work==False:
            print('抱歉，这句话我还不会回答')
            work = True
    elif flag == 'l':
        print("好的，下次再见")
        break			    #跳出整个循环
#其他情况，不能输入或输入非法信息时
    else:
        print("请输入提示的指令")
        continue
