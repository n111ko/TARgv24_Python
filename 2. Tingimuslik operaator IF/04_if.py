from random import *
from datetime import *
from calendar import *
from time import strptime

##### Ülesanne 1 #####

nimi = input("Mis on sinu nimi? ")

if nimi.isalpha() and nimi.isupper():
    if nimi == "JUKU":
        print("Lähme kinno")

        try:
            vanus = int(input(f"{nimi}, kui vana sa oled? "))
            if vanus < 0 or vanus > 100:
                print("Viga!")

            elif 6 <= vanus <= 14:
                print("Lastepilet")

            elif 15 <= vanus <= 65:
                print ("Täispilet")

            elif vanus > 65:
                print("Sooduspilet")

            else:
                print("Nii palju!!")

        except:
            print("Täisarv on vaja sisestada.")

else:
    print("Segatud sõne")

######################



##### Ülesanne 2 #####

nimi1 = input("Kirjuta oma nimi: ")
nimi2 = input("Kirjuta oma nimi: ")

nimed = ["Anton", "Viktor"]
if nimi1.isalpha() and nimi2.isalpha():
    if (nimi1 in nimed) and (nimi2 in nimed):
        print("Nad on pinginaabrid.")

    else:
        print("Nad ei ole pinginaabrid.")
else:
    print("Viga")

######################



##### Ülesanne 3 #####

try: 
    a = float(input("Kirjutage esimese seina pikkus: "))
    b = float(input("Kirjutage teise seina pikkus: "))

    kusimus = input("Kas te soovite remonti teha? (jah/ei)")

    if kusimus.upper() == "JAH" or kusimus.upper() == "J":
        ruutmeeteri_hind = float(input("Kui palju maksab ruutmeeter? "))

        poranda_hind = (a * b) * ruutmeeteri_hind

        print(f"Põranda vahetamise hind on {round(poranda_hind, 2)}.")

    elif kusimus.upper() == "EI" or kusimus.upper() == "E":
        print("Nägemist.")

    else:
        print("Viga")

except:
    print("On vaja numbreid sisestada!")

######################



##### Ülesanne 4 #####

try:
    hind = float(input("Sisestage hind: "))

    if hind > 700:
        soodustus = hind - (hind * 0.3)

        print(f"Hind soodustusega on {soodustus}.")

    else:
        print(f"Hind soodustuseta on {hind}.")

except:
    print("Viga")

######################



##### Ülesanne 5 #####

try:
    temperatuur = float(input("Sisestage temperatuur: "))

    if temperatuur >= 18:
        print("See on sobiv toasoojus.")

    else:
        print("Temperatuur on alla 18 kraadi.")

except:
    print("Viga")

######################



##### Ülesanne 6 #####

try:
    pikkus = float(input("Sisestage inimese pikkus (sm): "))

    if pikkus <= 150:
        print("See inimene on lühikest kasvu.")

    elif 151 <= pikkus <= 170:
        print("See inimene on keskmist kasvu.")

    elif 171 <= pikkus:
        print("See inimene on pikka kasvu.")

except:
    print("Viga")

######################



##### Ülesanne 7 #####

try:
    sugu = input("Kas te olete naine või mees? (N/M): ")

    if sugu.upper() == "NAINE" or sugu.upper() == "N":
        pikkus = float(input("Sisestage inimese pikkus (sm): "))

        if pikkus <= 150:
            print("Te olete lühikest kasvu.")

        elif pikkus <= 170:
            print("Te olete keskmist kasvu.")

        elif 171 <= pikkus:
            print("Te olete pikka kasvu.")

    elif sugu.upper() == "MEES" or sugu.upper() == "M":
        pikkus = float(input("Sisestage inimese pikkus (sm): "))

        if pikkus <= 160:
            print("Te olete lühikest kasvu.")

        elif pikkus <= 180:
            print("Te olete keskmist kasvu.")

        elif 181 <= pikkus:
            print("Te olete pikka kasvu.")

except:
    print("Viga")

######################



##### Ülesanne 8 #####

kusimus1 = input("Kas te soovite piima osta? (jah/ei): ")

if kusimus1.upper() == "JAH" or kusimus1.upper() == "J":
    piima_hind = randint(1, 5)

elif kusimus1.upper() == "EI" or kusimus1.upper() == "E":
    piima_hind = 0

kusimus2 = input("Kas te soovite mahla osta? (jah/ei): ")

if kusimus2.upper() == "JAH" or kusimus2.upper() == "J":
    mahla_hind = randint(1, 5)

elif kusimus2.upper() == "EI" or kusimus2.upper() == "E":
    mahla_hind = 0

kusimus3 = input("Kas te soovite šokolaadi osta? (jah/ei): ")

if kusimus3.upper() == "JAH" or kusimus3.upper() == "J":
    sokolaadi_hind = randint(1, 5)

elif kusimus3.upper() == "EI" or kusimus3.upper() == "E":
    sokolaadi_hind = 0

hind = piima_hind + mahla_hind + sokolaadi_hind

print()
print(f"Piim - {piima_hind}€\nMahl - {mahla_hind}€\nŠokolaad - {sokolaadi_hind}€")
print()
print(f"Hind on {hind}€.")

######################



##### Ülesanne 9 #####

try:
    a = float(input("Sisestage esimese külje pikkus: "))
    b = float(input("Sisestage teise külje pikkus: "))

    if a == b:
        print("See on ruut.")

    else:
        print("See pole ruut.")

except:
    print("On vaja numbreid sisestada!")

######################



##### Ülesanne 10 #####

a = float(input("Sisestage esimene arv: "))
b = float(input("Sisestage teine arv: "))

print()

kusimus = input("Mida te soovite teha? (+ | - | * | /): ")

if kusimus == "+":
    c = a + b

elif kusimus == "-":
    c = a - b

elif kusimus == "*":
    c = a * b

elif kusimus == "/":
    c = a / b

else:
    print("Viga")

#######################



##### Ülesanne 11 #####

sunnipaev = input("Sisestage oma sünnipäeva (DD-MM-YYYY): ")

sunnipaevv = datetime.strptime(sunnipaev, "%d-%m-%Y")
tana = datetime.today()
vanus = tana.year - sunnipaevv.year

if vanus > 0 and vanus % 10 == 0:
    print("Teil on juubel!")

else:
    print()
    print("Juubel mitte sellel aastal.")

#######################



##### Ülesanne 12 #####

hind = float(input("Sisestage hind: "))

if hind <= 10:
    hind = hind - (hind * 0.1)
    print(f"Teil on 10% allahindlus! Nüüd hind on {hind}.")

elif hind > 10:
    hind = hind - (hind * 0.2)
    print(f"Teil on 20% allahindlus! Nüüd hind on {hind}.")

else:
    print("Viga")

#######################



##### Ülesanne 13 #####

sugu = input("Kas te olete naine või mees? (N/M): ")

if sugu.upper() == "NAINE" or sugu.upper() == "N":
    print("Te ei sobi selle meeskonna jaoks.")

elif sugu.upper() == "MEES" or sugu.upper() == "M":
    vanus = input("Sisestage oma vanus: ")

    if 16 <= vanus <= 18:
        print("Te sobite selle meeskonna jaoks.")

    else:
        print("Te ei sobi selle meeskonna jaoks.")

else:
    print("Viga")

#######################



##### Ülesanne 14 #####

inimene = int(input("Kui palju inimesi tuleb? "))
buss = int(input("Mitu istekohta on bussis? "))

if inimene % buss == 0:
    print(f"On vaja {int(inimene/buss)} bussi.")
    print(f"Viimases bussis on {buss} inimest.")

elif inimene % buss != 0:
    print(f"On vaja {int(inimene/buss) + 1} bussi.")
    print(f"Viimases bussis on {inimene - (int(inimene/buss)) * buss} inimest.")

else:
    print("Viga")

#######################