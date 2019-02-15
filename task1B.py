fin1 = open("Book1.txt",'r')
for line in fin1:
	word1 = line.strip()
	print(word1)
fin2 = open("Book2.txt",'r')
for line in fin2:
        word2 = line.strip()
        print(word1)
fin3 = open("Book3.txt",'r')
for line in fin3:
        word3 = line.strip()
        print(word3)
d= dict()
for d in word1:
	if d in word2 and word3:
		print(d)

