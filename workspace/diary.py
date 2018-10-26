#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from Tkinter import *

root = Tk()
# 这居然是个x，26个英文字母
# 更改窗口大小
root.geometry('500x400')
# 定义标题
root.title("程序媛笔记本")
# 增加按钮和标签
saveBtn = Button(root,text="保存")
# btn.pack()表示把btn放在主窗口上，pack是一种布局方式
# 把按钮设置在左下
#  side 有4个值，TOP、BOTTOM、LEFT、RIGHT，默认为 TOP
#  anchor 是对齐方式，sw 即 southwest(西南)的，也就是左下
#  以此类推，一共有9个值 n、s、w、e、nw、sw、se、ne、center，默认是 cente
saveBtn.pack(side=LEFT,anchor='sw')

quitBtn = Button(root,text="退出")
quitBtn.pack(side=RIGHT,anchor='se')

writeBtn = Button(root,text="写日记")
writeBtn.pack(side=BOTTOM)

readBtn = Button(root,text="看日记")
readBtn.pack(side=BOTTOM)

# label可以通过config的方法设置文字
label = Label(root)
label.pack()
label.config(text = "这是一个演示程序")

# 写日记时 用到Entry和Text
# Entry 是一个简单的输入控件
# StringVar 是一个字符串变量类型
textVar = StringVar()
# textvariable 表示文本框中的值
# 写 textvariable=textVar 是为了方便我们后期对标题的一些操作
entry = Entry(root, textvariable=textVar)
entry.pack()
# Text 用来显示多行文本
text=Text(root)
text.pack()
root.mainloop()

# 看日记时 需要显示一个列表
# 用到 ListBox
# 默认列表高度太小，重新设置高度为300
listBox = Listbox(root,height=300)
listBox.pack()
# 设置一个数据源
# 数据源，变量，向列表中插入数据
list = ["apple","orange","milk","water"]
for item in list:                           # 遍历
    listBox.insert(0,item)

