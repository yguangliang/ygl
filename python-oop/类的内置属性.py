# 类的内置属性


class Person():
    """
    这是一个人类
    """
    name = "name"
    def work(self):
        print("上班")

# 通过类对象调用内置属性
print("Person.__dict__:", Person.__dict__)
print("Person.__doc__：", Person.__doc__)
print("Person.__name__：", Person.__name__)
print("Person.__bases__：", Person.__bases__)