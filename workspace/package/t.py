def cal(x,y):
    m = x+y
    return m

def test():
    #对模块中定义的函数调用进行测试
    print("模块测试结果",cal(3,4))
    #name就是获取了模块的名字。
    #当我们运行那个模块时，那个模块就是主程序。
    #如果我们调用这个模块，那这个模块就不是主程序了。
    #其他模块调用，就不会执行test()
if __name__=='__main__':
    #调用测试函数
    test()

