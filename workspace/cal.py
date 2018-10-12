#现在规定100分满分，90分及以上为A,70到90为B，60到70为C，60以下为D。
#写一个程序当输入分数时自动转换为ABCD并打印出来。
#elif，就是else if的意思。
grade = int(input("请输入分数"))
if 90<=grade<=100: 
    print("A")
elif 70<=grade<90:
    print("B")
elif 60<=grade<70:
    print("C")
else:
    print("D")
