def t(llista_alum):
	"""
	Retorna llista_alum[5,5,7]
	>>> t([2,3,7])
	[5, 5, 7]
	>>> t([35,-5000,71])
	[35, 5, 71]
	>>> t([-1,-2,-3])
	[5, 5, 5]
	"""
	for j in range (0,len(llista_alum)):
		if (llista_alum[j]<5):
			llista_alum[j]=5
	return llista_alum
	
	
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True) 



