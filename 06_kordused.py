# ##### Ülesanne 1 #####

# kogus = 0

# for i in range(15):
#     while True:
#         try:
#             arv = float(input("Sisestage arv: "))
#             break

#         except:
#             print("On vaja sisestada arv. Proovige uuesti.")
#             print()

#     if arv == int(arv):
#         kogus += 1

# print(f"Täisarve: {kogus}.")

# ######################



# ##### Ülesanne 2 #####

# while True:
#     try:
#         A = int(input("Sisestage arv: "))
#         break
    
#     except:
#         print("On vaja sisestada arv. Proovige uuesti.")

# summa = 0

# if A > 0:
#     for i in range(1, A+1, 1):
#         summa += i
#         print(f"{i}. samm = {summa}")

# print(f"vastus {summa}")

# ######################



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