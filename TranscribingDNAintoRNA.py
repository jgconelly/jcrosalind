#Transcribing DNA into RNA
#I tried to be clever here, but there was a much simpler way to do this in python. Using a simple string replace is enough for this exercise.
#def dnatorna(s):
#	rna = []
#	for letter in s:
#		if letter == "T":
#			rna.append("U")
#		else:
#			rna.append(letter)	
#	print(str(rna))

#

def dnatorna(s):
	print (s.replace("T", "U"))

dnatorna("ACAATTGCCGCGCGGCCTTCCATCCTTTACATTATACCGTGGAGGATAATGCAAAGAACTAGGTGACTGGCAATTTAGAGGAACACGGAAGATCTGTACACTCACGAGTGTTTGCATTATTTAGACCTTATACAGGACAGCGTATGCCTTTTTCAACGTCTAATAAAACGGCTTTCACATCTATCGCTTTAGCTAGCTACTCGCGACAGCTCGTAACGGTTCTGACTCTAGCATGTAACCTTCCTACTCCACGGGATGTTCGTTCATGACGGACTACTAACCACAAGAACTACTAACGGACGATGCCGATTAGTAGGCTCCGTGGCTCGCTGACCAATTGCTTAGTAAACTACGCATCTGCCCCAGTCGAACAGAGCTTGTACGCCGATCTATTTACTTATACTTATAGGTAACAATGCCTCGGAATAAGAACCTTCAAGCGGTTTAAGTCGTTATCTATTAACATTTTCACGCTAACTATCATTCGAGAAGTTCCGAGTATGTCAAGTGCTCCACGAAGCTTTCACCCGAATGCCGCTCTTTATAGTTTCCGTTTTCGTAGGCCTGCTGAGATGGTAAATATTCAAAAACCCCATCGGTCGATTGGCCTCGTACAGGTCCTCGGTCACTAGGCTGCGATGTTAAGCAAGTTCGACTGGAGATTGCGCGAATACGGGGATTTCTCGCGGGAAGGCTTTGACATCTCAGTCTCCGTGGTTAAACAGGTTGTCAACTTATATATCAGCAGTGTAAGGCATGGTTGAGTTCTTAAGGGGGGTAGTGTGTTGACTCTTATAGAATCTTTGCCATTCATTTGCATTCGACAAGGGTGACGAACCGGTGGAGTTTAGATGCTCGGAAGAAAATTTGAAACCACCCATAACGTATTCGGACATTCTGGTCTTTTACGGGATGGTTTATGATCGGCTTCACTACCGTGGCGGTCGGAGGCCGCTCCGTAAGA")