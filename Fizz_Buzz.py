"""
编写一个程序，打印1到100之间的数。
当这个数同时是3和5的倍数时候，打印FizzBuzz
当这个数只是3的倍数时候，打印Fizz
当这个数只是5的倍数的时候，打印Buzz
"""
def FizzBuzz():
	for i in range(1,101):
		if i%3 == 0 and i%5 == 0:
			print("FizzBuzz")
		elif i%3 == 0:
			print("Fizz")
		elif i%5 == 0:
			print("Buzz")
		else:
			print(i)

FizzBuzz()