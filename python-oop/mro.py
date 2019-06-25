# __mro__
# 返回一系列的父类，第一个为本身，第二为父类，依次往上知道object

# 创建一个Dog类的父类
class Animal():
    pass

# 子类继承父类
class Dog(Animal):
    pass

print(Dog.__mro__)
print(Animal.__mro__)
