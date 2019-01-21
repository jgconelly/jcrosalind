"""
Problem 
---------------------------------------
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; 
the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def countingdna(dna_sample):
	"Function to count the number of times the symbols occur"
	count_dictionary = {}
	for letter in dna_sample:
		if not letter in count_dictionary:
			count_dictionary[letter] = 1
		else:
			count_dictionary[letter] += 1

	for count in sorted(count_dictionary):
		print (count_dictionary[count])

countingdna("GTTTCGGGTCACGGCTGTAATTATTGTTCAACGTAGCAGGGGGACTCCGGTTGCAGCATGGGTACTCTTACCGCCATATACGAAGCGAACAAGCCGCCTTCATTTATACGTACGTCGTGCTATA"
	"TTGTCGGCGGTGATTTAATGACTGACTGAGAGAGCATCCTCAATGCCACGGCAGCAGATGATTCCTATTCCCGCGGTAGGCTATATGCGTGGAACGCACCCGTCGCCGGCATTATTGGGTCATTCGATGATGG"
	"GAGCGTCTTACAGCTCAGGTTACGCACTTGATCTCTCTAATTCAGTCACAAAATCACCCTCAGTCCTGTGCGCCAAGTAGCGATGACCGAGCCGCAAGGTGACACGGTTAATATACGTAAGTTTTGGTAACCC"
	"GGGCAACTTCCACATTGCCGAGTATAGTGCAGCAACTGTCACAGATAGAACGGTCAATCTGATGTCGCAACGTTCCTGGGCGAGAACAGTGTTCAAGGGACTAAGATCTAAGCATCGATCGCCAGAATTACTC"
	"AAGCGAAGCCGACCAATGTACGATATAAAGCAGGAAAGGATATATGCAGGTTGGTAGACCAGACTACTTTTCAAGTAGCAATAACGTTCTAACGTCTCGAGAACCAGAATGTGATAGGTCGCATCCTCCCCTA"
	"AGGGCACAAAGCATCGCCTGACATTCATGAGCCACACTCCCCCCGCGTGTACCAACTATAGGAGTCCACTGGTCTTATATTGTTCATACCTGATTCACCTCTAGATAAAGAACACGTTGAGAAAGGTGCGGCA"
	"AGACGAAGGCAAAGGGTCATCTAGTATGTACCAACAGTTCAAATTCTCCACTTGCATGCTCAGCTTCGTCCGCGGGCACGTCGAAAGGTTGATTCAAG")