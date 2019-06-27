# 成员描述符
# property函数
class Person():
    # 函数名称可以随便起
    # 以下三个函数都是对name(可控制属性值：_name)进行操作
    def fget(self):
        # 将名字*2
        return self._name

    def fset(self, name):
        # 将名字大写
        self._name = name.upper()

    def fdel(self):
        del self._name

    name = property(fget, fset, fdel, "对name进行下操作")

# 实例化对象
person1 = Person()
person1.name = "ygl" # 调用fset方法
print(person1.name)
