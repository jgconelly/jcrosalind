from itertools import permutations
import numpy as np
np.set_printoptions(threshold=np.inf)

def egd(number):
	perms = list(permutations(range(1, number + 1)))
	print (len(perms))
	array_perms = np.array(perms)
	semi_perms = str(array_perms).replace("[", "")
	final_perms = semi_perms.replace("]", "")
	print (mas_perms)

egd(6)