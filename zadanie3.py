# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:38:40 2022

@author: Magda
"""

"""
1. Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie go
wyświetlić ( print )
"""

def funkcja(name: str, surname: str) -> str:
    zmienna = f"Czesc {name} {surname}!"
    return zmienna

print(funkcja("Magda", "D"))

"""
2. Stworzyć funkcję, która przyjmie 2 argumenty typu int , a następnie zwróci wynik
mnożenia obu liczb.
"""

def mnozenie(x:int, y:int)->int:
    return y*x
print(mnozenie(3,5))

"""
3. Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
"Liczba nieparzysta"
"""

def czyParzysta(liczba:int) -> bool:
    if (liczba % 2 == 0):
        return True;
    else:
        return False;
    
sprawdzenie = czyParzysta(6)
    
if (sprawdzenie == True):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

"""
4. Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
jako typ logiczny bool"
"""

def sprawdzCzy1i2Wieksze(x: int, y: int, z: int) -> bool:
    if (x+y >= z):
        return True;
    else:
        return False;

sprawdzCzy1i2Wieksze(3,4,9)

"""
5. Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int. 
Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.
"""

lista=[4,5,6,2]
x=2

def czyZawiera(lista: list, x:int) -> bool:
    if (x in lista):
        return True
    else:
        return False

czyZawiera(lista,x)

"""
6. Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
"""

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8,9]

def zlaczListy(lista1: list, lista2: list) -> list:
    lista3= lista1+lista2
    lista3 = set(lista3)
    wynik = []
    for el in lista3:
        el = el ** 3
        wynik.append(el)
    return wynik
    
zlaczListy(lista1, lista2)











