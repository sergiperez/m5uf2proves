#encoding: utf8

def aprova(llista):
	"""
	Retorna 5
	>>> aprova ([1,5,7])
	[5, 5, 7]
	>>> aprova ([5,8,10])
	[5, 8, 10]
	>>> aprova ([1,2,3])
	[5, 5, 5]
	"""
	for i in range (0,len(llista)):
		if (llista[i]<5):
			llista[i]=5
	return llista

if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True)
