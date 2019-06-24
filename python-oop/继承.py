# 继承的语法
# 在python 中，任何类都有一个共同的父类叫Object
# 创建一个父类
class Person():
    name = "NoName"
    age =  0
    def sleep(self):
        print("Sleeping .... ....")

# 父类写在括号内
class Teacher(Person):
    pass

# 验证是否继承是这样写，如果可以调用父类的成员属性和方法，那么确定是这样的
# 我们定义一个子类的对象，调用父类里面的方法和属性
teacher1 = Teacher()
if teacher1.age == 0 and teacher1.name == "NoName" :
    teacher1.sleep()
    print("父类写在括号里面")
else:
    print("父类不写在括号里面")


