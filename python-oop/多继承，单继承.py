# 多继承和单继承例子

# 创建三个类

# 鱼类
class Fish():
    # 创建构造函数
    def __init__(self,name):
        self.name = name
    # 创建一个鱼类自己的函数
    def Swimming(self):
        print("Fish can swim!!")

# 鸟类
class Birds():
    # 构造函数
    def __init__(self,name):
        self.name = name
    # 平常函数
    def fly(self):
        print("Birds can flying!!")
# 人类
class Person():
    # 构造函数
    def __init__(self,name):
        self.name = name
    # 平常函数
    def working(self):
        print("Person can work!!!")

# 单继承:类的括号里面至于一个类，拥有父类的除了私有的方法之外的成员和方法
class SuperMan(Person):
    # 从写构造函数
    def __init__(self,name):
        self.name = name
    # 继承和从写平常函数
    def working(self):
        super().working()
        print("SurperMan can work!!")

# 多继承：类的括号里面有多个类，用逗号隔开，里面的类都是他的父类，拥有全部父类除了私有方法和成员之外的方法和变量的属性
class SuperWoman(Fish,Person,Birds):
    # 构造函数
    def __init__(self,name):
        self.name = name


# 创建单继承对象：调用构造函数来创建
print("创建单继承对象：调用构造函数来创建:")
SuperMan1 = SuperMan("xiaoming")
SuperMan1.working()
print()

# 创建多继承对象：调用构造函数来创建
print("创建多继承对象：调用构造函数来创建:")
SuperWoman1 = SuperWoman("小红")
# 调用第一个父类：Person的方法
SuperWoman1.working()
# 调用第二个父类方法：鸟类
SuperWoman1.fly()
# 调用第三个父类：鱼类
SuperWoman1.Swimming()
