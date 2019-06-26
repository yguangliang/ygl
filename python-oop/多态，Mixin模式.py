# Mixin其实就是多态的，只是里面有一些规定

# 创建一个人类
class Person():
    name = None
    age = 18
    def help(self):
        print("helping")

# Mixin创建一个鸟类：只有功能也就是自己实现的方法，不借助于子类实现
class Birds():
    def fly(self):
        print("flying")

# Mixin创建一个鱼类：只有功能，也就是自己实现的方法，不借助于子类实现
class Fish():
    def swim(self):
        print("swimming")

# 设计一个类，也就是多继承，除了第一份类，
# 后面的类只有单一的方法，他们的类中的方法也是自己实现的，没有借助子类来实现
# 超人类:这时候此类的对象就具有继承类的属性和方法，Mixin是单一的方法，
# 所以除了第一个，后面的都是单一的方法，也就是说没有那个类的影响只是少了几个功能而已
class SuperMan(Person,Fish,Birds):
    pass

# 创建一个超人类实例对象
superMan1 = SuperMan()
# 具有Person的属性和方法
print("具有Person的属性和方法")
print("superMan1.name:",superMan1.name)
print("superMan1.age:",superMan1.age)
print("superMan1.help():",end=" ")
superMan1.help()
print()

# 具有Fish的方法
print("具有Fish的方法:")
print("superMan1.swim():",end=" ")
superMan1.swim()
print()

# 具有Birds的方法
print("具有Birds的方法:")
print("superMan1.fly():",end=" ")
superMan1.fly()
print()