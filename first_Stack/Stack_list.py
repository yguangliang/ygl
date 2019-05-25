class myStack(object):
	"""docstring for myStack"""
	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		last = len(self.items) - 1
		return self.items[last]

	def size(self):
		return len(self.items)

#定义一个栈对象
myStack = myStack()
#定义一个列表
list1 = [1, 2, 3, 4, 5]
#将列表元素加入栈
for item in list1:
	myStack.push(item)
#打印栈中是否加入了列表
print(myStack.items)
#逆序列表
for i in range(myStack.size()):
	list1[i] = myStack.pop()
#输出逆序列表
print(list1)