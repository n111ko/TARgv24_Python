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



######################
