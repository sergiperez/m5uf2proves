#!/usr/bin/env python
# -*- coding: utf-8 -*-
def sumar(numero1,numero2):
	"""
	>>> sumar(5,5)
	10
	"""
	resultat=numero1+numero2
	return resultat
def restar(numero1,numero2):
	"""
	>>> restar(10,5)
	5
	"""
	resultat=numero1-numero2
	return resultat
def multiplicar(numero1,numero2):
	"""
	>>> multiplicar(2,4)
	8
	"""
	resultat=numero1*numero2
	return resultat
def dividir(numero1,numero2):
	"""
	>>> dividir(10,2)
	(5, True)
	"""
	if numero2==0:
		return 0,False
	resultat=numero1/numero2
	return resultat,True
repetircalculadora="si"
while repetircalculadora=="si":
	num1=int(raw_input("Introduce el numero 1: "))
	operador=raw_input("Introduce el operador: ")
	num2=int(raw_input("Introduce el numero 2: "))
	if operador=="+":
		print sumar(num1,num2)
	if operador=="-":
		print restar(num1,num2)
	if operador=="*":
		print multiplicar(num1,num2)
	if operador=="/":
		res,ok=dividir(num1,num2)
		if ok:
			print res
		else:
			print "Error no se puede dividir entre 0"
	repetircalculadora=raw_input("Quieres volver a calcular algo? ")
if __name__ == "__main__":
	import doctest
	doctest.testmod(verbose=True) 
