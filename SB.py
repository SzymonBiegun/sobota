'''Zadanie 1
Napisz program umożliwiający obliczenie ile paliwa spala samochód na 100 km.
 Dane wczytane to zużyte paliwo 22 litry i przejechana trasa 600 km.'''
'''
l=22
km=600
wynik=float(l/km*100)
print('Spalanie to: ',wynik)
'''
###########################################################
'''Zadanie 2.
 Mając daną wartość a=2 zwiększ jej wartośc o 10, następnie zmiejsz o 3.
Podnieś do potęgi drugiej a na koniec podziel przez 3. Wyświetl każdy z etapów.'''
'''
a=2
a+=10
print(a)
a-=3
print(a)
a**=2
print(a)
a/=3
print(a)
'''
###########################################################
'''Zadanie 3.
Napisz program wczytujący wartość a z klawiatury. Program zwraca informację a<0, a=0, a>0'''
'''
a=int(input('Podaj zmienna a: '))

if a<0:
    print("a<0")
elif a==0:
    print('a=0')
else:
    print('a>0')
'''
###########################################################
'''Zadanie 4.
 Napisz program z użyciem for liczący od 1 do wartości podanej z klawiatury.'''
'''
x=int(input("Podaj ostatnia wartosc: "))
i=0
for i in range(1,x+1):
    print(i)
'''
###########################################################
'''Zadanie 5.
 Napisz program z użyciem pętli while liczący od 1 do wartości podanej z klawiatury.'''
'''
i=0
x=int(input("Podaj ostatnia wartosc: "))
while i<x:
    print(i+1)
    i+=1
'''
###########################################################
'''Zadanie 6.
 Napisz program z wykorzystaniem dowolnej pętli sumujący 3 liczby wczytane z klawiatury'''
'''
a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
c=int(input("Podaj trzecią liczbę: "))
suma=0
for i in range(1):
    suma=a+b+c
    print(suma)
'''
###########################################################
'''Zadanie 7.
 Napisz program liczący od 1 do 10 i pomijający wyświetlenie cyfry 6'''
'''
i=1
for i in range(1,11):
    if i !=6:
        print(i)
'''
###########################################################
'''Zadanie 8.
 Napisz program z użyciem for liczący od 10 do 1 co 1'''
'''
i=1
for i in range(10,0,-1):
    print(i)
'''
###########################################################
'''Zadanie 9.
 Mając listę o nazwie samochod=['audi','fiat',citroen','peugeot'] wykonaj:
a)pokaż element 1 listy
b)skasuj element 2 listy'''
'''
lista=['audi','fiat','citroen','peugeot']
print(lista[0])

lista.pop(2)
print(lista)
'''
###########################################################
'''Zadanie 10.
Zadanie 9 Mając krotke o nazwie samochod=('audi','fiat','citroen','peugeot') wykonaj:
a)pokaz ostatni element krotki'''
'''
krotka=('audi','fiat','citroen','peugeot')
print(krotka[3])
'''
###########################################################



