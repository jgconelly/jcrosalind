import itertools
import numpy as np
#np.set_printoptions(threshold=np.inf)

def ogo(number):
	computation = []
	positive = list((range(1, number + 1)))
	negative = list((range(-1, -(number + 1), -1)))
	combined = negative + positive
	final = list(itertools.permutations(combined, number))
	#print (len(perms))
	#print (list(final))
	#print (positive)
	#print (negative)
	#print (len(final))
	print (final)
	print (len(final))
ogo(2)