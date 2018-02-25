#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funciones5.py
#  
#  Copyright 2018 cf17eric.visier <cf17eric.visier@super-desktop>

def A(nom,lletra):
	contador=0
	valor=lletra
	for i in nom:
			if i==valor:
				contador=contador+1
		
	return contador
	

    
n = raw_input("Introdueix una paraula: ")
l = raw_input("Introdueix una lletra: ")

print A(n,l)
 
