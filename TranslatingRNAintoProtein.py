#Translating RNA into Protein

def removeLineBreaks():
	f = open("/Users/Azreal/Desktop/RNACodonTable.rtf", "r")
	contents = f.read()
	string_fixed = contents.replace("	","")
	print (string_fixed)
removeLineBreaks()

#def translateRNA(s):
