"""
变位词
"""

def anagram(word1, word2):
	word1 = word1.lower()
	word2 = word2.lower()
	return sorted(word1) == sorted(word2)
print("anagram和amanagr是不是变位词?")
print(anagram("anagram","amanagr"))