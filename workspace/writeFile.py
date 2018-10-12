#编写一个程序，接受用户输入的内容。
#然后保存为新的文件。
#用上之前学过的input()，再用f.write()把内容写进文件。

#先用input()获取用户输入。
#用f.write()把内容写入文件。
text = input("请输入要写入文件的内容：")
filename = input("请输入文件名")
f = open(filename,'w')
f.write(text)
f.close()
