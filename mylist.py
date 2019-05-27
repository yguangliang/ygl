"""
列表
"""
#创建一个列表有两种方法
fruit1 = list()
print("第一种方法创建一个列表：")
print(fruit1)

print("第二种方法创建一个列表：")
fruit2 = []
print(fruit2)

#用len()函数获取list 列表的元素个数
fruit2 = [0, 1, 2, 3, 4]
print("列表fruit2：")
print(fruit2)
print("列表fruit2的元素个数：")
print(len(fruit2))

#利用索引访问列表中的每一个元素,超出索引会报：indexerror
#正整数索引，从0开始
print("列表中的第一个元素:"+ str(fruit2[0]))
print("列表中的超出的索引：str(fruit2[6])超出索引会报：indexerror")

#负数索引，-1表示最后元素，从右往左，依次减一，超出索引会报：indexerror
print("列表中的最后一个元素str(fruit2[-1])："+ str(fruit2[-1]))
print("列表中的超出的索引：str(fruit2[-5])超出索引会报：indexerror")



