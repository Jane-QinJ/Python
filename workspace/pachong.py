from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
#进入豆瓣图书top250官网
browser.get('http://book.douban.com/top250')

for i in range(0,10):
    #得到标题
    title = browser.find_element_by_xpath("//div[@id='content']//h1").text
    #打印标题
    print(title)
    #获得当前页面图书信息的元素对象的列表，总共有25条
    book_list = browser.find_elements_by_xpath("//tr[@class='item']")
    for ele in book_list:
        file = open('test.txt','w')
        file.write(ele.text + '\n')
    #输出当前页数
        print("----第%s页-----"%(i+1))

    #下一页
    next_page = browser.find_element_by_class_name("next").click()
    time.sleep(5)
    print("\n")
    
browser.quit()
file.close()
