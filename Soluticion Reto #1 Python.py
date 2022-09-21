# /*
#  * Reto #1
#  * ¿ES UN ANAGRAMA?

#  * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
#  * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
#  * NO hace falta comprobar que ambas palabras existan.
#  * Dos palabras exactamente iguales no son anagrama.

#####Maybe I can make a class to be able to scalate
from pickletools import string1


class Conversion:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.Unicode1 = []
        self.Unicode2 = []

    def stringToUnicode1(self, string1):
        for itemOfstring1 in string1:
            self.Unicode1.append(ord(itemOfstring1))
            ####Covert string caracther to Unicode
            # x = ord("h")
        return self.Unicode1

    def stringToUnicode2(self, string2):

        for itemOfstring2 in string2:
            self.Unicode2.append(ord(itemOfstring2))
        return self.Unicode2


def anagrama(stringOne, stringTwo):
    x = len(stringOne)
    y = len(stringTwo)
    ####Covert string caracther to Unicode
    # x = ord("h")
    counter = 0

    if x == y:
        for item in stringOne:
            for item2 in stringTwo:
                if item == item2:
                    counter += 1
        if counter == x:
            return True
        else:
            return False
    return False


palabra1 = Conversion("string1", "string2")
stringOne = palabra1.stringToUnicode1("Omar")
stringTwo = palabra1.stringToUnicode2("rOma")
print(stringOne)
print(stringTwo)


print(anagrama(stringOne, stringTwo))
