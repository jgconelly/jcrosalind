def removeLineBreaks():
	f = open("/Users/Azreal/Downloads/rosalind_gc2.txt", "r")
	contents = f.read()
	string_fixed = contents.replace("\n","")
	print (string_fixed)
removeLineBreaks()