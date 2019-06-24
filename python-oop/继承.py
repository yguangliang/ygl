# 继承的语法
# 在python 中，任何类都有一个共同的父类叫Object


# 创建一个父类
class Person():
    # 子类会改变的属性
    height = 160
    name = "NoName"
    # 私有的属性:在属性前面添加两个下划线
    __age = 0
    # 受保护的属性:属性前面加一个下划线
    _sex = None
    def sleep(self):
        print("Sleeping .... ....")

# 子类：是谁的子类？父类写在括号内
class Teacher(Person):
    # 子类改变父类的属性
    height = 180
    # 子类独有的属性：多态
    love = "student"
    # 子类独有的方法：多态
    def working(self):
        print("loving student! ")
    # 扩充父类的方法
    def sleep(self):
        super().sleep()
        print("loving studing! ")

print("Person.__dict__:",Person.__dict__)
print("Teacher.__dict__:",Teacher.__dict__)
# 验证是否继承是这样写，如果可以调用父类的成员属性和方法，那么确定是这样的
# 我们定义一个子类的对象，调用父类里面的方法和属性
teacher1 = Teacher()
person1 = Person()
print("teacher1.__dict__：",teacher1.__dict__)
print("Person.name的id:",id(Person.name))
print("person1.name的id:",id(person1.name))
print("Teacher.name的id:",id(Teacher.name))
print("teacher1.name的id:",id(teacher1.name))
print("说明子类在不进行从定义成员变量时候，是引用父类成员变量")
print("Person.height的id:",id(Person.height))
print("person1.height的id:",id(person1.height))
print("Teacher.height的id:",id(Teacher.height))
print("teacher1.height的id:",id(teacher1.height))
print("说明子类和父类同时拥有属性值不一和方法体不一时候，子类优先调用自己的属性和方法：这也是多态的体现")
teacher1.sleep()

print("*"*20)
# 构造函数的例子
class Dog():
    #  创建的构造函数
    def __init__(self):
        print("现在创建了一个实例化对象，所以调用了构造函数;")
# 使用构造函数创建对象
dog1 = Dog()
print("type(super):",type(super))
