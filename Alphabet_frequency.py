"""
字母频数
"""
def Alphabet_frequency(string):
	dic_count = {}
	for i in string:
		if i in dic_count:
			dic_count[i]+=1
		else:
			dic_count[i] =1
	print(dic_count)

string = "ssssgdfegfgvfgvrqqfn"
Alphabet_frequency(string)