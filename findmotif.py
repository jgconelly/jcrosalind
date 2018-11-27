import re

def findMotif(motif, dna):
	p = re.compile('dna*', re.IGNORECASE)
	print (p.search(motif))

findMotif("ATAT", "GATATATGCATATACTT")