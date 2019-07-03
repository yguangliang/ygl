# 变量的三种用法

class Person():
    # 魔法方法
    def __init__(self):
        self.name = "ygl"
        self.age = 18

    # 魔法函数
    def __getattr__(self, item):
        print("没有这个属性")

# 实例化对象
person1 = Person()

# 属性的三种用法：
# 1.赋值
person1.name = "yangguangliang"

# 2.读取
print(person1.name)
# 3.删除
del person1.name
print(person1.name)