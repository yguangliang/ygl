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


