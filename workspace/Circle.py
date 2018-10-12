class Circle:
	pi=3.14
	#如果你在类中定义了__init__()这个方法，创建对象时，Python会自动调用这个方法。我们也把这个过程叫做初始化。
                #在定义方法时，必须有self这一参数。这个参数表示某个对象。
	def __init__(self,radius):
		self.radius = radius
	def getArea(self):
		return area
#self在类的语句里就代表着类的一个对象。
#当我们创建了对象c，那么此时在类里面self就是指c
#创建类的一个对象c后，c就有了类的方法。
c = Circle(2)
print(c.getArea())
