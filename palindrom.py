"""
回文词
"""
def palindrom(word):
	#忽略大小写
	word = word.lower()
	#判断是否回文字
	return word[::-1] == word

string1 = "mum"
print(string1+"是回文字吗？")
print(palindrom(string1))