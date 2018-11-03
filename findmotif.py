import re

def findMotif(motif, dna):
	p = re.compile('dna*', re.IGNORECASE)
	print (p.search(motif))
	#m = p.search(dna)
	#iterator = p.finditer(dna)
	#for match in iterator:
	#	print (match.start())

	#thing = re.findall(motif, dna)

findMotif("ATAT", "GATATATGCATATACTT")