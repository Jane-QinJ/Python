import random
number = random.randint(1,10)
for i in range(1,10):
    print("猜猜看，这个数字是：")
    guess = int(input())
    if guess>number:
        print("太大了")
    elif guess<number:
        print("太小了")
    else:
        print("输入正确，你一共猜了"+str(i)+"次")
        break
print("游戏结束")
