print("----欢迎进入通讯录-----")
print("----1.查找联系人--------")
print('----2.退出通讯录---------')
print('----3.增加通讯录---------')
print('----4.删除通讯录---------')

contact= {'lily':'123456','mike':'1323232','jane':'1233444'}
#while True的意思是要一直进行循环，也就是死循环。要想停止它，可以用CTRL+C来终止循环。
#循环中的3个循环控制语句，break，continue和pass
#pass是空语句，不做任何事情，是为了保持程序结构的完整性。
#通常while True 会加入break用来在循环内部达成某个条件时终止循环。
#不然while True:在条件是真时就会一直循环，根本停不下来。
while True:
    num = int(input("请输入指令数字："))
    if num == 1:
        name = input("请输入联系人姓名：")
        #判断contact里面是否存在name
        if name in contact:
            print(name,":",contact[name])
            #continue跳过当前循环块中的剩余语句，然后再进入下一次循环。
            continue
    if num == 3:
        name = input("请输入联系人姓名：")
        phone = int(input("请增添联系人电话："))
        contact[name]=phone
        print(contact)
    if num == 4:
        name = input("请输入要删除联系人姓名：")
        del contact[name]
        print(contact)
    if num == 2:
        #break则是会跳出 for 和 while 的循环体，不再循环了。
        break
print('感谢使用通讯录')
