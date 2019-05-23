"""
我的第一个栈
"""
class MyFirstStack(object):
	"""docstring for MyFirstStack"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		""" 判断栈是否为空"""
		return self.items == []

	def push(self,item):
		"""像栈顶添加一个元素"""
		return self.items.append(item)

	def pop(self):
		""" 向栈顶删除一个元素"""
		return self.items.pop()

	def peek(self):
		""" 找到栈的最后一个元素 """
		last = len(self.items) - 1
		return self.items[last]

	def size(self):
		return len(self.items)

#新建的栈是空的
MyFirstStack = MyFirstStack()
print(MyFirstStack.is_empty())

#向栈中添加元素
MyFirstStack.push(1)
print(MyFirstStack.is_empty())
print(MyFirstStack.size())

#移除最后一个元素，因为只有一个，所以调用is_empty()方法
MyFirstStack.pop()
print(MyFirstStack.is_empty())

#打印栈顶的元素，栈里面没有元素时候，下标会出错
MyFirstStack.push(1)
print(MyFirstStack.peek())

#打印栈的大小
print(MyFirstStack.size())

#空栈
MyFirstStack.pop()
for c in "hello":
	MyFirstStack.push(c)
revert = ""
for i in range(len(MyFirstStack.items)):
	revert += MyFirstStack.pop()
print(revert)
