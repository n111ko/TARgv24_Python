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
