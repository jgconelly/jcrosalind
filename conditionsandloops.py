#conditions and loops
def sum_of_odd(a, b):
	x = 0
	for i in range(a,b):
		if i % 2 != 0:
			x = x + i
	print (x)

sum_of_odd(4214, 8428)


