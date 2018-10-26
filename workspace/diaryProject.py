#!/usr/bin/python
# -*- coding: utf-8 -*-
from Tkinter import *
import os
#写日记
def write():
	textVar.set("")				#清空entry
	text.delete("0.0","end")	#清空text
	label.config(text="写日记模式")
	listBox.pack_forget()		#隐藏listBox
	entry.pack()				#显示entry
	text.pack()					#显示pack
#保存
def save():
	title = textVar.get() + ".txt"    #获取标题
	content = text.get("0.0","end")

	if title != ".txt":
		fileObj = open(title,"wb")		#打开一个文件
		fileObj.write(content)			#写入内容
		fileObj.close()					#关闭打开的文件
		label.config(text = "已保存")
	else:
		label.config(text="请输入标题")

def read():
	listBox.delete(0,END)				#清空listBox
	dir = os.getcwd()					#获取当前目录
	list = os.listdir(dir)				#获取目录内所有文件

	showText = "看日记模式"
	if len(list) == 0:					#如果当前没有日记
	    showText += "(日记本是空的)"		#设置提示
	label.config(text=showText)

	for item in list:					#遍历
		listBox.insert(0,item)			#向listBox插入数据

	listBox.bind('<Double-Button-1>',showDiary)	#绑定双击事件

	entry.pack_forget()					#隐藏entry
	text.pack_forget()					#隐藏text
	listBox.pack()						#显示listBox

#显示日记内容
def showDiary(event):
	title = listBox.get(listBox.curselection()) #获取点击的日记名
	showTitle = title[:-4]						#截取至倒数第4个字符
	textVar.set(showTitle)						#设置日记标题

	fileObj = open(title,"r+")					#打开对应标题的文件
	content = fileObj.read()					#获取文件内容
	text.delete("0.0","end")					#清空 text
	text.insert("end",content)					#把内容显示在text上
	fileObj.close()								#关闭打开的文件

	listBox.pack_forget()						#隐藏listBox
	entry.pack()								#显示entry
	text.pack()									#显示 text
#创建日记文件夹
def initDiary():		
	dir = os.getcwd()			#获取当前.py 文件目录
	list = os.listdir(dir)		#获取当前目录中所有文件
	haveDiary = False			#设置一个变量，是否存在diary文件夹，默认为False
	for item in list:			#遍历
		if item == "diary":		#判断是否存在diary文件夹
			haveDiary = True		#如果有，设置diary为True
	if haveDiary == False:		#如果haveDiary为False
		os.mkdir("diary")		#创建diary文件夹

	os.chdir("./diary") 		#改变.py工作目录到diary内
initDiary()
# 需要的控件
root = Tk()
root.geometry('500x400')
root.title("程序媛日记本")

saveBtn = Button(root,text="保存",command=save)
saveBtn.pack(side=LEFT, anchor='sw')

quitBtn = Button(root,text="退出",command=quit)
quitBtn.pack(side=RIGHT,anchor='se')


#command = write表示点击按钮时 会执行write方法
writeBtn = Button(root,text="写日记", command=write)
writeBtn.pack(side=BOTTOM,anchor='s')


readBtn = Button(root,text="看日记",command=read)
readBtn.pack(side=BOTTOM,anchor='s')

textVar = StringVar()
entry = Entry(root,textvariable=textVar)
text = Text(root)
listBox = Listbox(root,height = 300)

label = Label(root)
label.pack()


root.mainloop()
