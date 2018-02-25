#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funciones5.py
# 
#  Copyright 2018 cf17eric.visier <cf17eric.visier@super-desktop>
def A(nom,lletra):
    """
    Retorna el nombre de vegades que es repeteix una lletra
    >>> A(" ", 'b')
    0
    >>> A("eric", 'b')
    0
    >>> A("eric", 'e')
    1
    """
    contador=0
    valor=lletra
    for i in nom:
        if i==valor:
            contador=contador+1
    
        return contador
 
    
 
if __name__ == "__main__":
        import doctest
        doctest.testmod(verbose=True)
