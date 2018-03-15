def producte(llista):
	'''
	Retorna el producte més alt dels dos nombres de la llista
	>>> producte(llista2)
	12
	'''
	M = llista
	resultat = []
	for i in llista:
		for j in M:
			if i != j:
				x = i*j
				resultat.append(x)        
	return max(resultat)
llista2=[2,6,1,2]
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True) 
