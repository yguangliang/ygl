"""
递归算法：通过调用自身函数来实现
l. 递归算法必须有终止条件。
2. 递归算法必须改变自己的状态，不断靠近终止条件。
3. 递归算法必须递归地不断调用自己。
"""
def bottles_of_beer(bob):
	if bob < 1:
		print("""
			no bottle of beer on the wall lyrics,no more bottles of beer""")
		return
	temp = bob 
	bob -= 1
	print("""{} bottle of beer on the wall ,
		{} bottles of beer. 
		take one down, pass it around ,
		{} bottles of beer on the wall""".format(temp,temp,bob))
	bottles_of_beer(bob)
bottles_of_beer(99)
