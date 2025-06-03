import random

sisselogimised = [] # логины
paroolid = [] # пароли

# проверка пароля
def parool_kontroll(parool:any) -> bool:
    """
    Parooli kontrollimine, kas see sisaldab numbreid, suuri ja väikeseid tähti ning erimärke
    :param any password: Sisestatud parool
    :rtype bool: Tagastab True, kui parool vastab kõikidele nõudmistele
    """

    if not any(char.isdigit() for char in parool): # проверка на наличие цифр
        return False
    if not any(char.isupper() for char in parool): # проверка на наличие заглавных букв
        return False
    if not any(char.islower() for char in parool): # проверка на наличие строчных букв
        return False
    spets_sumbolid=".,:;!_*-+()/#¤%&" # проверка на наличие хотя бы одного специального символа
    if not any(char in spets_sumbolid for char in parool):
        return False

    return True

# автоматическая генерация пароля
def genereeri_parool(pikkus = 12) -> any:
    """
    Genereerib automaatselt parooli, mis sisaldab numbreid, tähti ja erimärke
    :param int pikkus: Parooli pikkus, vaikimisi 12 tähemärki
    :rtype any: Tagastab genereeritud parooli
    """

    # 1-й вариант, более надежный пароль
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    # из списка извлекается 12 произвольных значений
    uus_parool = ''.join([random.choice(ls) for x in range(12)])
    # пароль готов

    return uus_parool

# создать или сгенерировать пароль
def loo_voi_genereeri_parool() -> any:
    """
    Parooli loomine või automaatne genereerimine
    :rtype any: Tagastab loodud või genereeritud parooli
    """

    print("\n1 - Automaatne parooli genereerimine\n2 - Sisestage parool ise")
    while True:
        valik_parool = input("Vali parooli loomise viis:(1 või 2): ")
        if valik_parool == "1":
            uus_parool = genereeri_parool() # ф-ция автоматической генерации пароля
            print(f"\nTeie uus parool on: {uus_parool}")
            return uus_parool
        elif valik_parool == "2":
            while True:
                uus_parool = input("Sisestage uus parool: ")
                if parool_kontroll(uus_parool): # ф-ция проверки пароля
                    return uus_parool
                else:
                    print("Parool peab koosnema numbritest, väiketähtedest, suurtähtedest ja erimärkidest!")
        else:
            print("Valige 1 või 2!")

# регистрация
def registreeri_kasutaja() -> bool:
    """
    Registreerib uue kasutaja, kui tema kasutajanimi pole veel olemas, ja genereerib parooli
    :rtype bool: Tagastab True, kui registreerimine on edukas
    """

    while True:
        uus_login = input("Sisestage uus kasutajanimi: ")
        if uus_login in sisselogimised:
            print("Selline kasutaja on juba olemas! Proovige uuesti!")
        else:
            break

    sisselogimised.append(uus_login) # новый логин добавляется в список зарегистрированных
    uus_parool = loo_voi_genereeri_parool()
    paroolid.append(uus_parool) # новый пароль добавляется в список зарегистрированных
    print(f"\nTe olete edukalt registreeritud!") 
    return True 

# ввод логина
def sisesta_login(sisselogimised:any) -> any:
    """
    Võimaldab sisestada kasutajanime ja kontrollib, et see on olemas
    :param any sisselogimised: Kasutajanimede nimekiri
    :rtype: any Tagastab sisestatud kasutajanime
    """

    while True:
        vana_login = input("Sisestage kasutajanimi: ")
        if vana_login not in sisselogimised: # проверяем, зарегестрирован ли пользователь
            print("Kasutajanimi ei leitud. Proovige uuesti!")
        else:
            return vana_login

# ввод пароля
def sisesta_parool(sisselogimised:any, paroolid:any, vana_login:any) -> any:
    """
    Võimaldab sisestada parooli ja kontrollib, et see vastab õigele kasutajale
    :param any sisselogimised: Kasutajanimede nimekiri
    :param any paroolid: Paroolide nimekiri
    :param any vana_login: Kasutajanimi, mille jaoks parooli kontrollitakse
    :rtype: any Tagastab õige parooli
    """

    while True:
        vana_parool = input("Sisestage parool: ")
        if vana_parool in paroolid and vana_login in sisselogimised: # проверка входит ли пароль и логин в списки рарегестрированных
            if paroolid.index(vana_parool) == sisselogimised.index(vana_login): # проверка, позиция пароля = позиции логина, т.е. пароль принадлежит логину
                return vana_parool
            else:
                print("Vale parool! Proovige uuesti!")
        else:
                print("Vale parool! Proovige uuesti!")

# изменить имя или пароль
def muuda_kasutaja_andmeid()->bool:
    """
    Võimaldab muuta kasutajanime või parooli
    :rtypebool: Tagastab True, kui andmed on edukalt muudetud, vastasel juhul False
    """

    # перед тем, как менять данные пользователя, нужно узнать его нынешние данные, чтобы изменить на нужные позиции в списке
    vana_login = sisesta_login(sisselogimised)
    index_login = sisselogimised.index(vana_login) # позиция логина в списке

    vana_parool = sisesta_parool(sisselogimised, paroolid, vana_login)
    index_parool = paroolid.index(vana_parool) # позиция пароля в списке

    while True:
        print("\n1 - Kasutajanime muutmine\n2 - Parooli muutmine\n3 - Tagasi kodulehele")
        valik = input("Sisestage valik (1,2 või 3): ")

        if valik == "1":
            while True:
                uus_login = input("Sisestage uus kasutajanimi: ")
                if uus_login in sisselogimised:
                    print("Selline kasutaja on juba olemas!")
                else:
                    sisselogimised.pop(index_login) # удаление старого логина с его позиции
                    sisselogimised.insert(index_login,uus_login) # новый на ту же позицию
                    print("\nKasutajanimi muudetud edukalt!")
                    break

        elif valik == "2":
            uus_parool = loo_voi_genereeri_parool()
            paroolid.pop(index_parool) # удаление старого логина с его позиции
            paroolid.insert(index_parool,uus_parool) # новый на ту же позицию
            print(f"\nParool on muudetud edukalt!")
            break 

        elif valik == "3":
            print("\nTagasi kodulehele...")

            return False

        else:
            print("Viga! Sisestage 1, 2 või 3!")

    return True