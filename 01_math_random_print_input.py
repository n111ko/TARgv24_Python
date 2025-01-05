from random import *  #*-kõik funktsioonid, randint as rd funktsioonide ümbernimetus
#import random -> random.randint()
from math import *
from tkinter import * #pi kasutamiseks


##### Ülesanne 1 #####

print("Tere tulemast!")
nimi = input("Mis on sinu nimi? ").capitalize() #lower()-aaa,upper()-AAA,capitalize()-Aaa
print("Tere tulemast! Tervitan sind", nimi) 
print("Tere tulemast! Tervitan sind "+ nimi)
vanus = int(input("Kui vana sa oled? "))
print("Tere tulemast! Tervitan sind "+nimi+". Sa oled",vanus,"aastat vana.")
print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana.")

######################



##### Ülesanne 2 #####

vanus = 18
eesnimi = "Jaak" 
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus))

######################



##### Ülesanne 3 #####

kokku = randint(1,1000)
print(f"Kokku on {kokku} kommi")
kommi = int(input("Mitu kommi sa tahad? "))
kokku = kokku-kommi
print(f"Jaak on {kokku} kommi")

######################



##### Ülesanne 4 #####

print("Läbimõõdu leidmine ")
#l-ümbermõõt
l = float(input("Ümbermõõt: "))
d = l/pi
print(f"Läbimõõdu suurus on {round(d,2)}")

######################



##### Ülesanne 5 #####

print("Ristkülikukujulise sektsiooni diagonaali pikkus.")
N = float(input("Kirjutage esimese külje pikkus: "))
M = float(input("Kirjutage teise külje pikkus: "))
diagonaal = sqrt(N**2 + M**2)
print(f"Ristkülikukujulise sektsiooni diagonaali pikkus on {round(diagonaal, 2)}")

######################



##### Ülesanne 6 #####

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg

print(f"Sinu kiirus oli {round(kiirus, 0)} km/h")

######################



##### Ülesanne 7 #####

print("Aritmeetilise keskmine")
a = int(input("Sisesta esimene number: "))
b = int(input("Sisesta teine number: "))
c = int(input("Sisesta kolmas number: "))
d = int(input("Sisesta neljas number: "))
e = int(input("Sisesta viies number: "))
arit_kesk = (a + b + c + d + e) / 5
print(f"Aritmeetilise keskmine on {round(arit_kesk, 2)}")

# x = range(6)
# for n in x:
#   print(n)

######################



##### Ülesanne 8 #####
print("Konn")
print("     @..@", "\n" , "   (----)", "\n" ,"  ( \__/ )", "\n" ,'  ^^ "" ^^')
######################



##### Ülesanne 9 #####

print("Kolmnurga ümbermõõt")
a = int(input("Sisesta esimese külje pikkus: "))
b = int(input("Sisesta teise külje pikkus: "))
c = int(input("Sisesta kolmanda külje pikkus: "))
P = a + b + c
print(f"Kolmnurga ümbermõõt on {round(P, 2)}")

######################



#### Ülesanne 10 #####
print("Pitsa")
p = int(input("Kui palju inimesi tellis pitsa? "))

pitsa_hind = 12.90
jootraha = pitsa_hind * 0.10

taishind = pitsa_hind + jootraha
hind_uhele = taishind / p

print("Tšekk", "\n","-----------", "\n", f"Pitsa hind: {pitsa_hind}€", "\n",f"Jootraha: {round(jootraha, 2)}€", "\n", f"Inimeste arv: {p}", "\n", f"Hind ühele: {round(hind_uhele, 2)}€", "\n", "-----------")

###################### 