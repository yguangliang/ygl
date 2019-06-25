# 菱形继承：多个子类继承自同一个父类，多个子类被同一个子类继承
# 人类：
class Person():
    # 当我们还不确定写什么的时候，用pass:相当于一个占位符，
    # 这里表示人类中的代码，在方法体中就表示方法体
    pass

# 男人类：继承人类
class Man(Person):
    pass

# 女人类：继承人类
class Woman(Person):
    pass

# 孩子类：继承男人女人类
class children(Man,Woman):
    pass