from selenium import webdriver

d = webdriver.Chrome() #打开谷歌浏览器
d.get('http://www.qiushibaike.com') #访问糗事百科

main_content = d.find_element_by_id("content-left")
content = main_content.find_elements_by_class_name('content') #注意elements,返回的content是列表

for c in content:
    print(c.text) #用循环打印文本值
#最后退出，否则每次都打开一个浏览器，电脑会卡
d.quit()
