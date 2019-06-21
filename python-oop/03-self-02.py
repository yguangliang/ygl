# self 案例
# 创建一个student类
class Student():
    name = "ygl"
    age = 1

    # 构造方法
    def __init__(self):
        self.name = "yguangliang"
        self.age = 18

    # 实例对象方法：打印实例对象的名字和年龄
    def say(self):
        print("self.name:",self.name)
        print("self.age:",self.age)

# 建立一个老师类
class Teacher():
    name = "kongzi"
    age = 180

# 表示学生类的一个实例对象
student1 = Student()
# 此时系统会默认将student1作为参数传入方法
student1.say()

# 学生类的类对象按理来说他不能调用say方法，因为say方法为非绑定类方法，
# 但是我们仔细想了一下可知道，非绑定类方法其实是默认将实例对象直接传入方法之中，所以我们在用类对象调用费绑定类方法时候
# 我们手动给方法传入一个实例对象，这样类对象就可以访问费绑定类方法了,在这个时候，self就变成了实例化对象了
Student.say(student1)

# 既然在非绑定类方法中，可以通过直接传入实例对象作为参数来调用方法
# 那么当我们试着用类对象作为参数的时候，也可以调用此参数，只是这个时候，类对象里面所对应的的属性为类的属性
Student.say(Student)

# 同样，如果我想将方法里面的对象变为Teacher这个类的类对象，也是可以的，
# 最主要的一点是这两个类拥有同样的属性，所以可以这样用，这也是python种语法不太严谨，换做在其他语言中就是报错的
# 方法中调用的属性，另一个类中有这些属性，所以这些属性就位这个类对象的类中的相应的属性值
Student.say(Teacher)

# 以上代码，利用了鸭子模型
# 如果一个有脚，有翅膀的东西，那么我就认为他是鸭子，就是说我看见有这么一个东西，
# 他有这些属性了，即使不是鸭子，我也认为他是鸭子