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