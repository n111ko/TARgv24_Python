# https://moodle.edu.ee/mod/assign/view.php?id=1966729

from euroopa_riigid_module import *

riik_pealinn, pealinn_riik, riigid = failist_to_dict('7. Sõnastikud/riigid_pealinnad.txt')
riigid = list(riik_pealinn.keys())

while True:
    print("\n--- Euroopa riigid - sõnastik ---")
    print("\n1 - Sõnastik\n2 - Pealinna kuvamine\n3 - Riigi nimi kuvamine\n4 - Viga parandamine sõnastikus\n5 - Kontrollida sõnavara teadmisi\n6 - Lõpetamine")
    vastus = int(input("\nSisestage valik: "))

    # вывод словаря
    if vastus == 1:
        for key, value in riik_pealinn.items():
            print(f"{key} - {value}\n")

    # вывод столицы, если вводиться название государства (и добавление в словарь - если нет)
    elif vastus == 2:
        riik_pealinn=leia_linn_pealinn(riik_pealinn, "pealinn", '7. Sõnastikud/riigid_pealinnad.txt')

    # вывод государства, если вводиться столица (и добавление в словарь - если нет)
    elif vastus == 3:
        riik_pealinn=leia_linn_pealinn(riik_pealinn, "riik", '7. Sõnastikud/riigid_pealinnad.txt')

    # если пользователь находит ошибку в словаре, то у него есть возможность ее исправить
    elif vastus == 4:
        riik_pealinn=viga_parandus(riik_pealinn, '7. Sõnastikud/riigid_pealinnad.txt')
    
    elif vastus == 5:
        viktoriin(riik_pealinn)

    # выход из программы
    elif vastus == 6:
        print("\n--- Head aega! ---\nProgrammi lõpetamine...")
        break

    else:
        print("Viga! Valige tegevus!")