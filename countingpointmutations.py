def countingpointmutations(x, y):
	count = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			count += 1
	print (count)
countingpointmutations("CCGCGCCAGCCTCATAGTCCTCTCAGTATCTTGCATCTACACATGCCCCGGTAATTTGTTGCATACGCAACCAAACAGGAGATCCCGTCAGCTAAGGCCTCTATCGGACGACGTGATTAGTCTAGCGCACGGGGGTAGTAATGAGATGTACTCAAGCATGGGTCAAGGAAGACTTTTAATGAGCACAATGACCAGAGAAATCTGCAACATGGGGGCTCCGCTGGGTTACATTGGAGGTTTGTTGCGTTCGATGCCGGAAAGACTGCACAAATTTTTAATTCGACGAGTAAATATGCCTGTTGAGGTCGCGTACTGTTATGCTACAGACCCTAACGGAGAGGAGTACGTGCCGCCCCTGGATTGTGACACGGGAAGTGCCGGCTAGGACCACTTTCTCGGGACTCGTGGTGCAACTAATTAGCTCTACTACGGTGCAGGAGCTACAAGTGCGAATGCCGCGCATTCGTTTCGCCCGCCACCCAACGGATCAATCGTGTCCGGTTACGCTGGCGCGATTTGATCATAATTCTGGACCCGGCTTCCTCGATGAGATTGTAAAACAGTCGAAGAGAGGAGCTGTGCGTATCTACGAATGCACAGTAATAGTTGACAAAGAAGGCAATATCCAAATGGATGGGCGAACAGCCAGTACCTCCTGCGCTACAAGAGGGGTTGGGGAAGCGAGCAGTCGGGGCCGATGGCCCATCGCGCAATTAGCTGATTCTACATCGCCTATGTGCAAACATATAACGTGCTGTTCCGGACCAATCCTTTCATGAACTGCAACGGGATAGCCTGATGTTGGTACATCCGCAGACGAAGCCCATACCATCTAGTTCGCACCCGAAATCCCTCTCCTTTCATCGGACTTATCCTCTGGACTGCAGCGTAACTTTTAATTTGAAATTGAAATGGTGAGTGATATGCTAACGGGTACAAAGGCGTCCCGAGTGAGAACGCAGGTTCTAATATCCCAGCGGCCTTTTG", "GCGCGTACAACCAATAAGCTTGTCTGTAAAATACATCGTCACACGTTCAGTTAGCTCTGTTAGTCCTTTTCCCTACATGAGCTTCTACAGTTTCACACGTCGCGCGGGTGACAGGCTGAGGTTAGCGAACGGGGGAACAAATAAGTGAGACACAAGTATGCGAAAAGGAAGATTTTTACATAGTAATTTGTCGATGGAGATCGTCAACATGGACGGTGCTTCGGGTCAATACCCAGCGTCTATACAGATTCTGCCAGAACCACTGCCTAGTCTTGTTAATAGAGCAGGAACCATAGCCGTCCAGGCACACTGACGTACAGCAACCGACTTTCACTATAGGGAGTTAGGGATGGTCGGGGATCGTAACTAGGGAACAGCCGGTTAGGTCCACTGTGAAGAGGCACGTCGTAACACTAACTCTATCTGCCTCTACACGGGAGCAGTAAGGTTCAACTCAACAGGCTGGTCACGCTCCTTACTAGCTGAAGCTATCGTGTACTATCGCTATAGCGCTATCGGAGCCGATATTTAGAGGGGGTTTATTCACTTGGATCATAAAACCAACTAGGGGAGGACCTGTAGGACTAAACGTGTAGAACTTAGGAGTCGGACACCTATGATCTTAACAAATGAAGGTTCCAGGAACATCTTTCTGCTCATTTCCACTTGGGAAGGTGCCTACTAGGAGAGACAGAAGGCGTTTTATCGGGTATTTGTAAAACTGTACATCACGAATAGGCAAACATCTGGCGGGTAGTCTCGCAAAAATGGTCCGGTGTTACGCGAAGCCGCGTCCGTAGGTTGGTACCATCTCATCGCTAACACACGTGTTGAAGATAACTATCGAAAAGCTTGATCTCGCAACGGACGGCTCCATTAGACGCCAGCATAGGTAGTAACCCGTCGTTAGCTTGAGGCGTGAGGATCGTAGCGGTACACATCGGTCCAGTTTGGTGGAGCCACGTCTAGTCTCGTTTAGCGCGCTCG")		