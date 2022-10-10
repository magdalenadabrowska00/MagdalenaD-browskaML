# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:43:32 2022

@author: Magda
"""

"""
2.a
Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
wyświetli każde z nich.
"""

listaImion = ['Magda', 'Ania', 'Robert', 'Paulina', 'Julia']

def funkcjaImion(imiona):
    for imie in imiona:
        print(imie)

funkcjaImion(listaImion);

"""
b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5 dowolnych
liczb, każdy jej element pomnoży przez 2, a na końcu ją zwróci. Zadanie
należy wykonać w 2 wersjach:
i. Wykorzystując pętle for .
ii. Wykorzystując listę składaną.
"""

# i
listaLiczb = [4,3,7,6,1]

def funkcjaLiczby(lista):
    for liczba in lista:
        print(liczba*2)
   
funkcjaLiczby(listaLiczb)


#ii

listaLiczb = [4,3,7,6,1]

def funkcjaLiczby(lista):
    nowaLista = []
    for liczba in lista:
        nowaLista.append(liczba*2)
    return nowaLista
   
print(funkcjaLiczby(listaLiczb))

"""
c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
wykorzystanie funkcji range ), a następnie wyświetli jedynie parzyste elementy.
"""
lista = list(range(0,10,1))
def Parzyste (lista):
    for el in lista:
        if el % 2 == 0:
            print(el)
Parzyste(lista)

"""
d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb (rekomendowane
wykorzystanie funkcji range ), a następnie wyświetli co drugi element.
"""

lista1 = list(range(5,15,1))
#print(lista1)
def CoDrugiElement(lista1): 
    coDrugiElement = [lista1[index] for index in range(0, len(lista1), 2)]
    print(coDrugiElement)

CoDrugiElement(lista1)








