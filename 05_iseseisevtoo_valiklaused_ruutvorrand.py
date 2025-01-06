##### Ülesanne 1 #####

try:
    a = float(input("Sisestage number: "))

    if a > 0:
        print("See arv on positiivne.")

        if a % 2 == 0:
            print("See arv on paaris.")

        else:
            print("See arv on paaritu.")

    else:
        print("See arv on negatiivne.")

except:
    print("On vaja numbreid sisestada!")

######################

##### Ülesanne 2 #####

try:
    a = float(input("Sisestage esimene number: "))
    b = float(input("Sisestage esimene number: "))
    c = float(input("Sisestage esimene number: "))

    if a > 0 and b > 0 and c > 0:
        print("Need numbrid on positiivsed.")

        if a + b + c == 180:
            print("Need numbrid võivad olla kolmnurga nurgad.")

            if a == b == c:
                print("See on võrdkülgne kolmnurk.")

            elif a == b or a == c or b == c:
                print("See on võrdhaarne kolmnurk.")

            else:
                print("See on erikülgne kolmnurk.")
        else:
            print("Need numbrid ei saa olla kolmnurga nurgad, kuna summa ei ole 180.")

    else:
        print("Need numbrid on negatiivsed.")

except:
    print("On vaja numbreid sisestada!")

######################

##### Ülesanne 3 #####

question = input("kas soovite teada nädalapäeva nime numbri järgi? (jah/ei): ")

if question.upper() == "JAH" or question.upper() == "J":
    a = int(input("Sisestage number vahemikus 1 kuni 7: "))

    if a == 1:
        print("See on esmaspäev.")

    elif a == 2:
        print("See on teisipäev.")

    elif a == 3:
        print("See on kolmapäev.")

    elif a == 4:
        print("See on neljapäev.")

    elif a == 5:
        print("See on reede.")

    elif a == 6:
        print("See on laupäev.")

    elif a == 7:
        print("See on pühapäev.")

    else:
        print("Viga")

elif question.upper() == "EI" or question.upper == "E":
    print("Nägemist.")

else:
    print("Nägemist.")

######################

##### Ülesanne 4 #####

day = int(input("Sisestage oma sünnipäeva päev(1-31): "))
month = int(input("Sisestage oma sünnipäeva kuu(1-12): "))

if month == 1 and 1 <= day <= 20:
    print(f"Teie sünnipäev on {day}. jaanuaril ning teie sodiaagimärk on Kaljukits.")

elif month == 1 and 21 <= day <= 31:
    print(f"Teie sünnipäev on {day}. jaanuaril ning teie sodiaagimärk on Veevalaja.")

elif month == 2 and 1 <= day <= 20:
    print(f"Teie sünnipäev on {day}. veebruaril ning teie sodiaagimärk on Veevalaja.")

elif month == 2 and 21 <= day <= 29:
    print(f"Teie sünnipäev on {day}. veebruaril ning teie sodiaagimärk on Kalad.")

elif month == 3 and 1 <= day <= 20:
    print(f"Teie sünnipäev on {day}. märtsil ning teie sodiaagimärk on Kalad.")

elif month == 3 and 21 <= day <= 31:
    print(f"Teie sünnipäev on {day}. märtsil ning teie sodiaagimärk on Jäär.")

elif month == 4 and 1 <= day <= 19:
    print(f"Teie sünnipäev on {day}. aprillil ning teie sodiaagimärk on Jäär.")

elif month == 4 and 20 <= day <= 30:
    print(f"Teie sünnipäev on {day}. aprillil ning teie sodiaagimärk on Sõnn.")

elif month == 5 and 1 <= day <= 20:
    print(f"Teie sünnipäev on {day}. mail ning teie sodiaagimärk on Sõnn.")

elif month == 5 and 21 <= day <= 31:
    print(f"Teie sünnipäev on {day}. mail ning teie sodiaagimärk on Kaksikud.")

elif month == 6 and 1 <= day <= 21:
    print(f"Teie sünnipäev on {day}. juunil ning teie sodiaagimärk on Kaksikud.")

elif month == 6 and 22 <= day <= 30:
    print(f"Teie sünnipäev on {day}. juunil ning teie sodiaagimärk on Vähk.")

elif month == 7 and 1 <= day <= 22:
    print(f"Teie sünnipäev on {day}. juulil ning teie sodiaagimärk on Vähk.")

elif month == 7 and 23 <= day <= 31:
    print(f"Teie sünnipäev on {day}. juulil ning teie sodiaagimärk on Lõvi.")

elif month == 8 and 1 <= day <= 22:
    print(f"Teie sünnipäev on {day}. augustil ning teie sodiaagimärk on Lõvi.")

elif month == 8 and 23 <= day <= 31:
    print(f"Teie sünnipäev on {day}. augustil ning teie sodiaagimärk on Neitsi.")

elif month == 9 and 1 <= day <= 22:
    print(f"Teie sünnipäev on {day}. septembril ning teie sodiaagimärk on Neitsi.")

elif month == 9 and 23 <= day <= 30:
    print(f"Teie sünnipäev on {day}. septembril ning teie sodiaagimärk on Kaalud.")

elif month == 10 and 1 <= day <= 23:
    print(f"Teie sünnipäev on {day}. oktoobril ning teie sodiaagimärk on Kaalud.")

elif month == 10 and 24 <= day <= 31:
    print(f"Teie sünnipäev on {day}. oktoobril ning teie sodiaagimärk on Skorpion.")

elif month == 11 and 1 <= day <= 21:
    print(f"Teie sünnipäev on {day}. novembril ning teie sodiaagimärk on Skorpion.")

elif month == 11 and 22 <= day <= 30:
    print(f"Teie sünnipäev on {day}. novembril ning teie sodiaagimärk on Ambur.")

elif month == 12 and 1 <= day <= 21:
    print(f"Teie sünnipäev on {day}. detsembril ning teie sodiaagimärk on Ambur.")

elif month == 12 and 22 <= day <= 31:
    print(f"Teie sünnipäev on {day}. detsembril ning teie sodiaagimärk on Kaljukits.")

else:
    print("Viga")

######################

##### Ülesanne 5 #####

a = float(input("Sisestage arv: "))

if a.is_integer() == True:
    print("See on täisarv.")
    a = a * 0.50
    print(a)

elif a.is_integer() == False:
    print("See on murdarv.")
    a = round(a * 0.70, 2)
    print(a)

else:
    print("Viga")

######################

##### Ülesanne 6 #####

question = input("Kas te soovite ruutvõrrandi lahendada? (jah/ei): ")

if question.upper() == "JAH" or question.upper() == "J":
    a = float(input("Sisestage a: "))
    b = float(input("Sisestage b: "))
    c = float(input("Sisestage c: "))

    D = b**2 - 4 * a * c

    if D > 0:
        print("Võrrandil on 2 lahendust.")

        x1 = (-b + D**0.5) / (2 * a)
        x2 = (-b - D**0.5) / (2 * a)

        print(f"x1 = {x1}, x2 = {x2}")

    elif D == 0:
        print("Võrrandil on 1 lahendus.")

        x = -b / (2 * a)

    elif D < 0:
        print("Võrrandil pole lahendusi.")

    else:
        print("Viga")

elif question.upper() == "EI" or question.upper == "E":
    print("Nägemist.")

else:
    print("Nägemist.")

######################