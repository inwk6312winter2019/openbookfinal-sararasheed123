def count_the_article():
	fin = open("Book2.txt",'r')
	for line in fin:
		word = line.strip()
		print(word)
	count = 0
	if len(word) in count:
            		count[i] += 1
        else:
            		count[i] = 1
    	for item in count:
        	print(item)
count_the_article("Book2.txt",'r')

