# https://moodle.edu.ee/mod/assign/view.php?id=1713190

from isikukood_module import *

ikoodid = [] # правильные исикукоды
arvud = [] # неправильные исикукоды

# бесконечный запрос исикукодов
while True:
    try:
        ikood=input("\nSisestage isikukood (või sisestage 'X' lõpetamiseks): ")

        if ikood.lower()=="x":  # проверка команды выхода
            break

        # проверка на количество символов
        if not kontroll_pikkus(ikood):
            print("Isikukood peab sisaldama 11 numbrit!")
            arvud.append(ikood)
            continue

        # проверка первого символа и даты рождения (не родился ли человек в будующем)
        aasta,kuu,paev=leia_synniaeg(ikood)
        if not kontroll_synniaeg(aasta,kuu,paev):
            print("Vale sünniaeg isikukoodis!")
            arvud.append(ikood)
            continue

        sunniaeg=f"{paev}.{kuu}.{aasta}"

        # проверка контрольного числа
        kontroll_num=int(ikood[10])
        jaak=leia_kontroll_nr(ikood)
        if jaak!=kontroll_num:  # проверка, если остаток не равен контрольному номеру
            print("Vale kontroll number!")
            arvud.append(ikood)
            continue
        
        # определение места рождения
        sunnikoht_num=int(ikood[7:10])
        sunnikoht=leia_sunnikoht(sunnikoht_num)
        if sunnikoht=="Tundmatu sünnikoht":
            print("Vale sünnikoht!")
            arvud.append(ikood)
            continue

        # определение пола
        sugu=leia_sugu(ikood)

        print(f"See on {sugu}, tema sünnipäev on {sunniaeg}.\nSünnikoht on {sunnikoht}.")
        ikoodid.append(ikood)

    except:
        print("Sisestage isikukood!")

# сортировка списков
arvud.sort() # по возрастанию

# перебор всех элементов из списка ikoodid и создание списка из женских исикукодов, которые начинаются на 2,4,6
ikoodid_naised = [ikood for ikood in ikoodid if int(ikood[0]) in {2,4,6}]
# перебор всех элементов из списка ikoodid и создание списка из мужских исикукодов, которые начинаются на 1,3,5
ikoodid_mehed = [ikood for ikood in ikoodid if int(ikood[0]) in {1,3,5}]
# сначала искикукоды женщин, потом мужчин
ikoodid = ikoodid_naised+ikoodid_mehed

# вывод на экран обоих списков
print(f"\nÕiged isikukoodid: {ikoodid}")
print(f"\nVigased isikukoodid: {arvud}")
print()