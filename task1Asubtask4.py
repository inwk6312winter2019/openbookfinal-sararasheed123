def character_word_count (a):
	fin = open("Book1.txt",'r')
	for line in fin:
		word = line.strip()
		print(word)
	d =dict()
	for c in word:
        	print c, word[c]
character_word_count("Book1.txt")
