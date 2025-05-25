from datetime import *
from calendar import *
from random import *
from math import *

##### Ülesanne 1 #####

paevadekogus = monthrange(2024,11)[1] #calendar modulist
print(paevadekogus)

a = input("Kirjuta oma nimi: ")

tana = date.today() #nimetus()-funktsioon 
tanaf = tana.strftime("%B %d, %Y")

print(f"Tere {a}! Täna on {tanaf}.")

d = tana.day #nimetus - omadus 27
m = tana.month
y = tana.year
print(d)
print(m)
print(y)

detsP = monthrange(2024,12)[1] #31
novP = monthrange(2024,11)[1] #30
jaak = detsP+novP-d
jaak2 = novP-d

print(f"Aasta lõpuni on {jaak}.")
print(f"Kuu lõpuni on {jaak2}.")

######################



##### Ülesanne 2 #####

vastus1 = 3 + 8 / (4 - 2) * 4
vastus2 = 3 + 8 / 4 - 2 * 4
vastus3 = (3 + 8) / (4 - 2) * 4
vastus4 = round((3 + 8) / (4 - 2) * 4)
print(vastus1,"\n",vastus2,"\n",vastus3,"\n",vastus4)

######################



##### Ülesanne 3 #####

R = float(input("Sisestage R: "))

print()

ruudu_pindala = round((R * 2) ** 2, 2)
ruudu_umbermoot = round((R * 2) * 4, 2)
ringi_pindala = round(R * pi ** 2, 2)
ringi_umbermoot = round(2 * pi * R, 2)

print(f"Ruudu pindala on {ruudu_pindala}\nRuudu ümbermõõt on {ruudu_umbermoot}\nRingi pindala on {ringi_pindala}\nRingi ümbermõõt on {ringi_umbermoot}")

print()

######################



##### Ülesanne 4 #####

d=2.575 # mündi d sm +
maa=6378 #maa radius km
maa*=100000 #maa radius sm + maa=maa*100000
Lmaa=2*pi*maa

kogus=Lmaa/d

print(f"On vaja {int(kogus):,d} mündi.\nMeil on vaja {int(kogus*2):,d} eur")

######################



##### Ülesanne 5 #####

a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

######################