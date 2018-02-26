#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Intenta desecriptar text dintre de una llista, si pot torna cada valor de la llista desencriptat, si no torna una llista vuida
def desencripta_text(text_encriptat):
    """
    Cas 1
    >>> desencripta_text(['GnkZ'])
    ['Hola']

    Cas 2
    >>> desencripta_text([])
    []

    Cas 3
    >>> desencripta_text(["$"])
    []
    """
    text_desencriptat = []
    for linea in text_encriptat:
        intent, text = desencriptar(linea)
        if intent:
            text_desencriptat.append(text)
        else:
            return []
    return text_desencriptat

# Función que implementa el proces de desencriptació
def desencriptar(missatge):
    global SIMBOLS_ORIGINALS
    global SIMBOLS_TRANSFORMATS
    missatge_pla = ""
    for caracter in missatge:
        i = SIMBOLS_TRANSFORMATS.find(caracter)
        if i<0:
            return False,missatge_pla
        missatge_pla += SIMBOLS_ORIGINALS[i]
    return True,missatge_pla

SIMBOLS_ORIGINALS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .?"
SIMBOLS_TRANSFORMATS = "?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 ."
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(desencripta_text(input(": ").split()))
