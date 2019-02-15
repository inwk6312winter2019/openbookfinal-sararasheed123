def starts_with_vow(a,b,c):
	fin1 = open("Book1.txt",'r')
	for line in fin1 :
		word1 = line.strip()
		print(word1)
	fin2 = open("Book2.txt",'r')
        for line in fin2 :
                word2 = line.strip()
                print(word2)
	fin3 = open("Book3.txt",'r')
        for line in fin3 :
                word = line.strip()
                print(word3)
	
	if "a" and "e"  and "i" and"o" and "u" in word1:
		word1[i]+=0
	else:
		print(word1)
	if "a" and"e" and"i"and"o"and"u" in word2:
                word2[i]+=0
        else:
                print(word2)
	if "a"and"e"and"i"and"o"and"u" in word3:
                word3[i]+=0
        else:
                print(word3)
	sum1 = word1+word2+word3
	print(sum1)
starts_with_vow("Book1.txt","Book2.txt","Book3.txt")


