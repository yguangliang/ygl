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

#list是一个可变的有序表，可以往list中追加元素到末尾
fruit2.append(5)
print("往fruit2的末尾添加5:")
print(fruit2)

#把元素插入到指定的位置,指定位置的元素的索引向后移动一位
fruit2.insert(0, 0)
print(fruit2)

#list删除末尾元素
print("删除末尾元素:5")
fruit2.pop()
print(fruit2)

#删除指定位置的元素，指定位置的元素向前移动一位
print("删除索引为0元素:0")
fruit2.pop(0)
print(fruit2)

#替换索引为0的元素
print("替换索引为0的元素为:Zero")
fruit2[0] = "Zero"
print(fruit2)

#list元素的数据类型可以不一样
print("替换索引为1的元素为:一个列表")
fruit2[1] = [1, 2, 3]
print(fruit2)


