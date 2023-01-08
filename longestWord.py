def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word1) <= len(word2) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("by", "too", "thanks")) #thanks
print(longest_word("dear", "guy", "hello")) #hello
print(longest_word("tablet", "book", "doorknob")) #doorknob
