# 构造函数：实例化对像的时候回自动调用这个函数，不写的时候按照MRO调用
# 在类中从写构造函数，也就是方法的从写
# 当某个父类重写构造方法时候方法参数个数改变，和需要调用的对象的类冲突会报错，这时候按照提示输入参数即可

# 创建一个人类
class Person():
    # 创建实例化对象时候
    # 姓名确定
    # 年龄确定
    # 地址确定
    # 从写构造函数
    def __init__(self):
        self.name = "Person"
        self.age = 18
        self.address = "贵州"

    # 从写__str__方法，让其打印对象的时候打印属性而不是哈希地址，返回对象属性:str类型
    def __str__(self):
        # str方法将int转换为str类型，
        return "name:" + self.name + " " + "age:" + str(self.age) + " " + "address:" + self.address

# Man类继承Person,没有重写构造函数，当实例化对象时候，就会调用父类的
#  当然打印对象的时候没有重写__str__方法，所以这时候调用了父类的__str__方法
class Man(Person):
    pass

#  Woman类继承Person,重写构造函数，当实例化对象时候，就会调用自己的构造方法,
#  当然打印对象的时候，因为重写__str__方法，所以这时候调用了自己的__str__方法
class Woman(Person):
    # 重写构造方法
    def __init__(self, name):
        self.name = name
        self.age = 18
        self.address = "贵州"

    # 重写__str__方法
    def __str__(self):
        return "Woman"




# 实例化一个人
person1 = Person()
# 打印对象时候调用__str__方法
print("person1:",person1)
# 通过__dict__方法查看对象的属性
print(person1.__dict__)
# 实例化一个Man对象,由于没有重写__init__方法，会使用父类的构造方法
man1 = Man()
print("man1:", man1)

# 实例化一个Woman,因为自己重写了构造方法和__str__，所以用自己的
# 当某个父类重写构造方法时候方法参数个数改变，和需要调用的对象的类冲突会报错，这时候按照提示输入参数即可
woman1 = Woman("Woman")
print(woman1)
print(woman1.__dict__)