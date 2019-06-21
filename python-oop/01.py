"""
定义一个学生类，用来形容学生
"""


# 定义一个学生空类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass


# 定义一个学生对象
student1 = Student()


# 定义一个类：描述听python课程的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 0
    course = "Python"

    # 需要注意
    # 1.def doHomeWork 的缩进层次
    # 2.系统会默认出一个self参数
    def doHomeWork(self):
        print("做作业")

        # 推荐在函数末尾使用return语句
        return None


# 实例化一个叫做yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.age)
yueyue.doHomeWork()
