#首先我们确定六位数字密码，一共三次机会。
#随后我们要获取用户输入并且判断。
#循环也不要忘记break
#如果密码输入对了就跳出整个循环。

#规定6位数字密码是123456
psw= 123456
#一共有三次机会
count=3

while count:
    count -= 1
    pad = int(input("请输入密码"))
    if pad == psw:
        print("密码正确")
        break
    else:
        if count != 0:
            print("密码输入错误，你还有",count,"次机会。")
        else:
            print("密码输入错误。")

