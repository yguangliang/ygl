"""
我的第一个队列
"""
class FirstQueue:
	def __init__(self):
		self.items = []

	def is_empty(self):
		""" 检查队列状态，队列为空时返回True,反之则返回False"""
		return self.items == []

	def enqueue(self,item):
		"""向队列中添加一个元素"""
		self.items.insert(0,item)

	def dequeue(self):
		"""向队列中删除一个元素"""
		return self.items.pop()

	def size(self):
		"""返回队列中的元素的数量"""
		return len(self.items)

#新建一个队列
FirstQueue = FirstQueue()
#队列的状态
print(FirstQueue.is_empty())

#add a element to queue
FirstQueue.enqueue(1)
print(FirstQueue.size())

#add 5 element to queue
for i in range(5):
	FirstQueue.enqueue(i)
print(FirstQueue.size())

#Remove queue elements in turn
for i in range(5):
	print(FirstQueue.dequeue())
print()
print(FirstQueue.size())

