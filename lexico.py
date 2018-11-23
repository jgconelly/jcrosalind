import itertools
import numpy as np

def lexico(string, number):
	clean_string = string.replace(" ", "")
	result = itertools.product(clean_string, repeat=number)
	list_result = list(result)
	empty = []
	for item in list_result:
		empty.append(str(item))
	#although this looks gross, it does what I need it to. Getting rid of the extra characters from the list of lists is 
	#required to make this answer work. 
	for item in empty:
		new_item = ((((item.replace("(", "")).replace(")", "")).replace(", ", "")).replace("'", ""))
		print (new_item)

lexico('A B C D E F G H', 3)	
