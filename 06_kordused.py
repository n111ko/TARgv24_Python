##### Ülesanne 1 #####

kogus = 0

for i in range(15):
    while True:
        try:
            arv = float(input("Sisestage arv: "))
            break

        except:
            print("On vaja sisestada arv. Proovige uuesti.")
            print()

    if arv == int(arv):
        kogus += 1

print(f"Täisarve: {kogus}.")

######################



##### Ülesanne 2 #####

while True:
    try:
        A = int(input("Sisestage arv: "))
        break
    
    except:
        print("On vaja sisestada arv. Proovige uuesti.")

summa = 0

if A > 0:
    for i in range(1, A+1, 1):
        summa += i
        print(f"{i}. samm = {summa}")

print(f"vastus {summa}")

######################



##### Ülesanne 3 #####

p = 1

for i in range(8):
    while True:
        try:
            arv = float(input("Sisestage arv: "))
            break

        except:
            print("On vaja sisestada arv. Proovige uuesti.")

    if arv > 0:
        p *= arv

    else:
        print("Korrutame arvud ainult rohkem kui 0.")

    print(f"{i+1}. samm korrutis = {p}")

######################



##### Ülesanne 4 #####

for i in range(10, 21, 1):
    i2 = i ** 2

    print(f"{i} ** 2 = {i2}") #    print(f"{i} ** 2 = {i2}", end = "; ")

######################



##### Ülesanne 5 #####

N = int(input("Sisestage arvude arv: "))

summa = 0

for i in range(N):
    while True:
        arv = float(input("Sisestage arv: "))

        if arv < 0:
            summa += arv
            break

        else:
            print("Summeritakse ainult negatiivsed arvud.")

print(f"Summa = {summa}.")

######################



##### Ülesanne 6 #####

N = int(input("Sisestage arvude arv: "))

positiivne = 0
negatiivne = 0

for i in range(N):
    while True:
        try:
            arv = float(input("Sisestage arv: "))

            if arv > 0:
                positiivne += 1
                break

            elif arv < 0:
                negatiivne += 1
                break
        except:
            print("On vaja sisestada arv. Proovige uuesti.")
            print()

print()
print(f"Positiivsed arvud {positiivne}\nNegatiivsed arvud {negatiivne}")

######################



##### Ülesanne 7 #####

A = int(input("Sisestage vahemiku algus: "))
B = int(input("Sisestage vahemiku lõpp: "))
K = int(input("Sisestage number, millega jagada: "))

for i in range(A, B):
    if i % K == 0:
        print(i, end = "; ")

######################



##### Ülesanne 15 #####

for read in range(10):

    for veerg in range(10):
        print(read, end=" ")

    print()

print()

#######################



##### Ülesanne 16 #####

for j in range(1, 10):

    for i in range(1, 10):
        if i == j:
            print(j, end=" ")

        else:
            print("0", end=" ")

    print()

print()

#######################