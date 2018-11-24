import itertools
	
def new_lexico(string, number):
	all_perms = []
	clean_string = string.replace(" ", "")
	for i in range(1, number + 1):
		all_perms.append(list(map(''.join, (itertools.product(clean_string, repeat=i)))))
	permutations = list(itertools.chain(*all_perms)) #requires variadic arguments in order to work 
	sorted_empty = sorted(permutations, key=lambda perm: [string.index(c) for c in perm])
	for item in sorted_empty:
		new_item = ((((item.replace("(", "")).replace(")", "")).replace(", ", "")).replace("'", ""))
		print (new_item)

new_lexico('Y J N L A U T I X O S P', 3)