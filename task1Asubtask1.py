fin1 = open("Book1.txt",'r')
fin2 = open("Book2.txt",'r')
fin3 = open("Book3.txt",'r')

for line in fin1:
	word1 = line.strip()
	print(word1)

for line in fin2:
	word2 = line.strip()
	print(word2)

for line in fin3:
	word3 = line.strip()
	print(word3)
for item1 in word1:
	if len(item1) == 50:
		print(item1)
		break
	else:
		print(item1)



for item2 in word2:
        if len(item2) == 50:
                print(item2)
                break
        else:
                print(item2)

for item3 in word3:
        if len(item3) == 50:
                print(item3)
                break
        else:
                print(item3)


