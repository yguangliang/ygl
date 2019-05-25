"""
逆序输出yesterday
"""

class myStack(object):
	"""docstring for myStack"""
	def __init__(self, ):
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

#创建一个栈对象
myStack = myStack()
#将字符串输出栈中
for i in "yesterday":
	myStack.push(i)

#定义一个空字符串，将逆序的字符放入字符串
Reverse_order = ""

for i in range(myStack.size()):
	Reverse_order += myStack.pop()


print(Reverse_order)