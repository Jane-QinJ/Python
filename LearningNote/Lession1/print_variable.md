## Print方法与变量

### 第1节 Print 数字
Python是一门编程语言，很受欢迎呢
他可以做网站，做人工智能等等
print()是Python提供的一个方法，可以帮助我们输出括号里填写的内容
我们只要记住怎么用就可以了，print() 就是输出()里填写的

先输出一个6再输出一个2

以后我们有疑问的时候，就去写写代码看看是什么
print(6 2) 语法错误   invaild sytax  程序报错了，说明这样的格式不行，括号里面数字只能填一个

### 第2节 变量的命名与赋值
变量:
变量就是存储在内存中的值，它可以指定不同的数据类型，因此这些变量可以存储字符，整数或者小数等
Python包含五个标准的数据类型：它们是 Numbers(数字)，String(字符串)，List(列表)，Tuple(元组)和Dictionary(字典)
定义变量:
只需要记住 变量名是字母 数字 下划线的随意组合，开头是数字的就不符合
变量的赋值:
Python中的变量赋值无需声明类型，但是变量在使用前都必须赋值，因为只有变量赋值以后这个变量才会被创建
我们用等号=给变量赋值，=左边是变量名，=右边是储存在该变量中的值
a = 1 就是把1赋值给a， 程序中遇见 = ，是说右边计算的值赋给左边

我们可以把变量a看成一张空白的扑克牌，a = 1 就是把1写到a 上

print(a) 输出括号里的值，当括号里的值是变量时，输出的是变量存的值
print(a) 相当于扫描扑克牌a上的值
a = 1 执行完后，a上写的是1，扫描的结果就是1
print()里面是数值，能直接输出，如果是变量，则输出变量存储的值

### 第3节 改变变量值
变量之所以叫变量，就是可变的意思
a = 1 
a = 2
现在a是多少
遇到不清楚的，咱们就把他输出来看看 print(a) 结果为2


程序按从上到下执行， 先执行 a = 1
再执行 a = 2时，a中已经存储了1对吧
此时 a = 2 操作 2会覆盖之前存储的1
a = 2 相当于在扑克牌上擦掉1，新写进去2
4. 第4节 变量加减乘除
计算机最开始就是为了做运算，接下来我们就用程序实现
变量运算实质上是变量存储的值运算
a = 1
b = 2 
c = a + b


同理可得：
c = a- b c = a * b c = a/b

5. 第5节 改变变量自身的值
编程中，变量虽然是最基础的，但用法很多
通过变量本身改变变量的值
编程虽然有很多概念难以理解，遇到概念，动手写会更好

变量运算其实是变量存储的值运算

a = a + 1 其实等于 a = 1 + 1
同样，这个也适合其他四则运算