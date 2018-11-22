import itertools
import numpy as np
def lexico(string, number):
	result = itertools.product(string, repeat=number)
	list_result = list(result)
	chars = "(,')"
	empty = []
	for item in list_result:
		empty.append(str(item))

	final_list = [item.replace(chars, "") for item in empty if chars in item]
	for item in final_list:
		print (item)
	#print (list_result)

lexico('ABCDEFGH', 3)	
