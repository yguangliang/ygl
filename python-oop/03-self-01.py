# 创建一个学生类
class Student():
    # 编写成员变量
    name = "ygl"
    age = 18

    # 非绑定类方法
    def say(self):
        self.age = 17
        self.name = "yangguangliang"
        print("self.name:",self.name)
        print("self.age:", self.age)
        return None

    # 绑定类方法
    def sayAgain():
        print("这是一个绑定类方法")
        print("绑定类方法中访问类中的成员变量：__class__+ 类的属性")
        print("__class__.age = {0}".format(__class__.age))
        print("__class_.name = {0}".format(__class__.name))

student1 = Student()
student1.say()
print(student1.name,student1.age)
# student1.sayAgain()
Student.sayAgain()