# 私有变量案例

# 人类：
class Person():
    # 共有变量
    name = "ygl"
    # 私有变量
    __age = 18

# 实例化对象
person1 = Person()
# 访问公有对象
print("person1.name:",person1.name)
# 访问不了私有变量
# AttributeError: 'Person' object has no attribute '__age'
# print("person1.__age:",person1.__age)

# name mangling技术,其实就是将_age的名字改为了:_类名__age
print(Person.__dict__)

# 实例化对象重新赋值访问
person1._Person__age = 19

# 类对象直接访问
print(person1._Person__age)
print(Person._Person__age)