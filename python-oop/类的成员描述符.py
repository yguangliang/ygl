# 类的成员描述符

class Person():
    # 构造函数：实例化对象的时候调用这个函数
    # 类的方式
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.upperName(name)

    def upperName(self, name):
        # 让name 里面的字符串全部大写
        self.name = name.upper()

    # 打印对象的时候会调用这个方法:print(对象)
    def __str__(self):
        return "name:" + self.name + " " + "age:" + str(self.age)

# 创建一个实例对象
person1 = Person("ygl", 18)
print(person1)
