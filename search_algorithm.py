"""
顺序搜索
"""

def search_algorithm(numlist, n):
	#定义一个标签
	Find = False
	for n in numlist:
		Find = True
		return Find
	return Find

#定义一个字符串用来表示一组数
numlist = []
#定义一个需要查找的数字
n = 99
#向字符串中加入数
for i in range(1, 100):
	numlist.append(i)

print(search_algorithm(numlist,n))