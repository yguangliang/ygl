# 多继承中的MRO：其实MRO就是一个列表

# 人类：
class Person():
    # 当我们还不确定写什么的时候，用pass:相当于一个占位符，
    # 这里表示人类中的代码，在方法体中就表示方法体
    # 定义一个共同名字的方法
    def speak(self):
        print("Person can speak")
        return None
# 男人类：继承人类
class Man(Person):
    # 定义一个共同名字的方法
    def speak(self):
        print("Man can speak")

# 女人类：继承人类
class Woman(Person):
    # 定义一个共同名字的方法
    def speak(self):
        print("Woman can speak")

# 孩子类：继承男人女人类
class Children(Man,Woman):
    # 定义一个共同名字的方法
    def speak(self):
        super().speak()
        print("children can speak")

# 孩子类类对象使用mro
print("children1.__mro__:",Children.__mro__)
# 得到注释里面的内容：可以看到，第一个为本身，第二个为Man，也就是创建类的括号里面的继承顺序的第一个，然后是更高级一级的，最后是object
# children1.__mro__: (<class '__main__.Children'>, <class '__main__.Man'>, <class '__main__.Woman'>, <class '__main__.Person'>, <class 'object'>)

# 只有类对象才有__mro__方法，类对象没有此方法

