import random
#在1到10之间随机生成一个整数
number = random.randint(1,10)
print("我正在想一个1到10之间的整数")

for i in range(1,7):
    #猜6次
    print("猜猜看，这个数字是：")
    guess = int(input())
    if guess<number:
        print("太小啦！")
    elif guess>number:
        print("太大了")
    else:
        print("恭喜你，猜对啦。 你一共猜了"+str(i)+"次")
        #此时i是字符串格式
        break
    #break 是指跳出整个for循环
    #在不满足上述两个条件时，用break跳出整个for循环，不再进行循环
print("游戏结束")
