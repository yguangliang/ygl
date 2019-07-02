# 类和对象的三种方法
class Person():
    # 实例方法
    def shili(self):
        print("实例方法")
        print(self)

    # 类方法
    # 参数一般谢伟cls
    @classmethod
    def classMethod(cls):
        print("类方法")
        print(cls)

    # 静态方法
    # 没有参数
    @staticmethod
    def staticMethod():
        print("静态方法")

# 创建一个实例对象

# 实例方法的调用
person1 = Person()
person1.shili()

# 类方法的调用
Person.classMethod()

# 静态方法的调用
Person.staticMethod()