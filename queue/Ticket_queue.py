import time
import random

class Queue:
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

	def simulate_line(self, till_show, max_time):
		"""
		模拟向队伍出售电影票的场景
		till_show是整型，表示离电影开始还有多少秒
		max_time是整型，表示排队购票最长需要花多少秒
		"""
		#创建一个空队列和一个空列表，列表记录哪些人购买了电影票
		#向列表中添加100个字符串，从person0开始到person99结束
		#队列中的每个字符串表示一个正在排队等待购票的人
		pq = Queue()#新建一个队列，表示正在排队买票的人
		tix_sold = []#表示已经买到票的人

		for i in range(10):
			pq.enqueue("person" + str(i))

		t_end = time.time() + till_show#电影开始时间
		now = time.time()#现在时间
		while now <t_end and not pq.is_empty():#当电影还没开始或者还有人排队
			now = time.time()
			r = random.randint(0, max_time)#随机数
			time.sleep(r)#停止运行r时间
			person = pq.dequeue()#排队队列减去第一个人(第一个人买到票)
			print(person)#打印买到票的人
			tix_sold.append(person)#把买到票的人加入列表
		return tix_sold #函数返回买到票的列表

queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)
