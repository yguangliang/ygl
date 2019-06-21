"""
类对象和实例对象的区别：
类对象不会改变，如果实例对象不改变成员变量，则类对象与实例对象相等
实例对象会改变，通过实例化对象点操作符给成员变量赋值，此时类变量还是初始值，而实例化对象则是赋值的值
并且__dict__方法中不再为空，为所改变的成员变量的键值对
"""
# 新建一个类：student
class Student():
    name = "ygl"
    age = 18

    def working(self):
        print("I am working!")
        # 推荐在后面使用return
        return None

# 不改变成员变量
# 查看类对象的成员变量
print("1.不改变成员变量:")
print("     类对象属性Student.name:",Student.name)
print("     类对象属性id(Student.name):",id(Student.name))
print("     类对象Student.__dict__",Student.__dict__)
# 新建一个实例化对象
student1 = Student()
print("     实例化对象student1.name：",student1.name)
print("     实例化对象student1.name：",student1.name)
print("     类对象student1.__dict__",student1.__dict__)
print()

# 通过实例化对象改变成员变量
print("2.通过实例化对象改变成员变量:")
# 改变成员变量
student1.name = "yangguangliang"
student1.age = 17
print("     实例化对象student1.name：",student1.name)
print("     实例化对象student1.name：",student1.name)
print("     类对象student1.__dict__",student1.__dict__)
print()
# 查看类对象的成员变量
print("     类对象属性Student.name:",Student.name)
print("     类对象属性id(Student.name):",id(Student.name))
print("     类对象Student.__dict__",Student.__dict__)
