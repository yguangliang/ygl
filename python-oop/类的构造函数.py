# 类的构造函数
class Perspon():
    name = "ygl"
    # 构造函数
    def __init__(self):
        print("我是一个人类")

    def __call__(self):
        print("__call__被调用")

    def __str__(self):
        return "__str__被调用"

    # 访问一个不存在的属性时候触发，当属性存在的时候，直接调用属性的值，不存在属性调用此方法，打印属性的默认值：None
    def __getattr__(self, item):
        print("__getattr被调用")

    def __setattr__(self, key, value):
        # 以下这句的意思是给这个对象赋值，但是给对象赋值的时候就会又调用这个函数，所以是一个死循环
        # 在Python中，递归的深度最大默认为1000，所以这里会出现报错
        # self.key = value
        # 为了避免上面的情况我们调用父类的方法
        super().__setattr__(key,value)



# 新建一个类
class Cat():
    # 构造函数
    def __init__(self, name):
        self._name = name

    # 当执行大于运算的时候调用
    def __gt__(self, other):
        return self._name > other._name

# 所谓的不需要人为调用就是不做 对象.方法名 就可以调用方法
# 创建一个实例对象，这里创建一个实例化对象,在创建实例化对象的时候自动调用了魔法方法
# 调用__init__
person1 = Perspon()

# 调用__call__
person1()

# 调用__str__
print(person1)

# 调用__getattr__
print(person1.name)

person1.name = "ygl"
print(person1.name)
# 不同对象的属性不同
person2 = Perspon()
print(person2.name)

cat1 = Cat("cat1")
cat2 = Cat("cat2")
print(cat1>cat2)
