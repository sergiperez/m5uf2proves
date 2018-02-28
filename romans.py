'''
http://codingdojo.org/kata/RomanNumerals/
https://remonsinnema.com/2011/12/05/practicing-tdd-using-the-roman-numerals-kata/
'''
def transformar(nombreArab):
    '''
     >>> transformar(1)
     'I'
     >>> transformar(2)
     'II'     
    '''
    if nombreArab == 2:
        return 'II'
    else: 
        return 'I' 
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()