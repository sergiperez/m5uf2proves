#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Genera una llista amb el que introdueixi lusuari. Afegint tantes lineas com s'hagi indicar al parametre
def CrearLlista(num_text):
    """
    Cas 1
    >>> len(CrearLlista(0))
    0

    Cas 2
    >>> len(CrearLlista(1))
    1
    """
    text = []
    for i in range(num_text):
        #text.append(input("Escriu una linea: "))
        text.append(str(i))

    return text

# S'imprimeix una cada valor d'una llista indicant la seva posicio començant amb 1
def ImprimirLlista(text):
    for i in range(len(text)):
        print(i + 1, text[i])
    return

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    num_text = int(input("Escriu un enter: "))
    text = CrearLlista(num_text)
    ImprimirLlista(text)
