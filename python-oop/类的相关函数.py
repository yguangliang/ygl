# 类的相关函数
class A():
    pass

class B(A):
    name = "ygl"

class C():
    pass

class D():
    pass

# issubclass(B ,A)
print("B是A的子类：验证如下")
print("issubclass(B ,A):",issubclass(B,A))
print("issubclass(C ,A):",issubclass(C, A))
print()

# isinstance():判断一个对象是否是一个类的实例对象，如果他是一个类的实例对象，那么他也是这个类的父类的实例对象
b = B()
print("b是B类的对象：验证如下")
print("isinstance(b ,B):",isinstance(b ,B))
print("isinstance(b,A):",isinstance(b ,A))
print("isinstance(C,C):",isinstance(C ,C))
print()

# hasattr(a,b):检测a对象是否有b成员
print("hasattr(a,b):检测a对象是否有b成员:")
print("hasattr(b,name='name'):", hasattr(b, "name"))
print("hasattr(b,name='age'):", hasattr(b, "age"))
print()

# 想知道某个函数怎么用
# help函数
# 例如
print("用help函数知道gerattr方法的具体用法：help(getattr)")
help(getattr)
print()

# dir(a)：获取对象的方法列表
d = D()
print("dir：获取对象的方法列表:")
dir(d)
