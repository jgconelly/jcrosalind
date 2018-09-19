#reading and writing
def evenlines():
	file = open("/Users/Azreal/Downloads/rosalind_ini5.txt", "r")
	i = 1
	for line in file.readlines():
		if i % 2 == 0:
			print (line)
		i += 1 
evenlines()