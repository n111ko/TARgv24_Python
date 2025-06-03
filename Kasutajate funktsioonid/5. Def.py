from datetime import *
from calendar import *
from def_module import *

######################

a = int(input("Sisestage arv1: "))
b = int(input("Sisestage arv2: "))
c = input("Sisestage arv3: ")

vastus = summa3(a, b, int(c))
print(vastus)

######################



##### Ülesanne 1 #####

k1 = float(input("Sisestage esimene arv: "))
k2 = float(input("Sisestage teine arv: "))
k3 = str(input("Sisestage argument: "))

vastus = arithmetic(k1, k2, k3)
print(round(vastus, 2))

######################



##### Ülesanne 2 #####

year = int(input("Sisestage aasta: "))

vastus = is_year_leap(year)
print(vastus)

######################



##### Ülesanne 3 #####

k = float(input("Sisestage külje pikkus: "))

vastus = square(k)
print(vastus)

######################



##### Ülesanne 4 #####

kuu = int(input("Sisestage kuu number: "))

vastus = season(kuu)
print(vastus)

######################



##### Ülesanne 5 #####

eur = float(input("Sisestage mitu euro: "))
aasta = int(input("Sisestage aasta: "))

vastus = bank(eur, aasta)
print(round(vastus, 2))

######################



##### Ülesanne 6 #####

arv = int(input("Sisestage arv: "))

vastus = is_prime(arv)
print(vastus)

######################


##### Ülesanne 7 #####

paev = int(input("Sisestage päev: "))
kuu = int(input("Sisestage kuu: "))
aasta = int(input("Sisestage aasta: "))

vastus = date(paev, kuu, aasta)
print(vastus)

######################