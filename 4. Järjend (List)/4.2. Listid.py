import string

# https://moodle.edu.ee/mod/assign/view.php?id=1449749

##### Ülesanne 1 - Sõna/Lause #####

# Sisestage sõna või lause klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on. Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.

vokaali = ["a", "e", "u", "o", "i", "ü", "ö", "õ", "ä"]
konsonanti = "qwrtpsdfghjklzxcvbnm"
markid = string.punctuation

while True:
	v = k = m = t = 0
	tekst = input("Sisesta mingi tekst: ").lower()
	
	if tekst.isdigit():
		break
	
	else:
		tekst_list = list(tekst)
		print(tekst_list)
		
		for taht in tekst_list:
			if taht in vokaali:
				v += 1
			elif taht in konsonanti:
				k += 1
			elif taht in markid:
				m += 1
			elif taht == " ":
				t += 1
				
		print("Vokaali: ", v)
		print("Konsonanti: ", k)
		print("Markid: ", m)
		print("Tühikud: ", t)
		
##### Ülesanne 2 - Loetelu #####

# Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi. Lisa võimalist loendis olevaid nimesid muuta.

# Loo kood, mis ei väljasta kordusi. 

# Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine.

for i in range(5):
	nimi = input(f"Sisesta nimi {nimi + 1}: ")
	nimed.append(nimi)

print("Enne sorteerimist: ", nimed)
nimed.sort()
print("Pärast sorteerimist: ", nimed)
print(f"Viimane lisatud nimi: {nimi}")

v = input("Kas muudame nimeid? y/n").lower()
if v == "y":
	v == input("Nimi või Positsioon (N/P): ").upper()
	if v == "N":
		v = int(input("Sisesta nime asukoht: "))
		uus_nimi = input("Uus nimi: ")	
		nimed[v - 1] = uus_nimi
		print(nimed)
	else:
		vana_nimi = input("Sisesta vana nimi: ")
		v = nimed.index(vana_nimi)
		uus_nimi = input("Siesta uus nimi: ")
		nimed[v] = uus_nimi
		print(nimed)

# dublikat 1
dublikat = list(set(nimed))
print(dublikat)

#dublikat 2
dublikat = []

for nimi in nimed:
	if nimi not in dublikat:
		dublikat.append(nimi)
		
print("Mitte korduv loetelu 2.variant")
print(dublikat)


vanused = []

for i in range(7):
	vanus = int(input(f"{i + 1}. Vanus: "))
	vanused.append(vanus)

print(f"Sisestatud vanused: {vanused}")
print(max(vanused)) # max arv
print(min(vanused)) # min arv
print(sum(vanused)/len(vanused)) # keskmine arv

##### Ülesanne 3 - Tärnid #####

# Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm. Näiteks:
# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************

vartused = [11, 24, 5, 68, 17]
s = "*"

for vartus in vartused:
	print(vartus)
	

##### Ülesanne 4 - Postiindex #####

# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:

# 1 – Tallinn
# 2 – Narva, Narva-Jõesuu
# 3 – Kohtla-Järve
# 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
# 5 – Tartu linn
# 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
# 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
# 8 – Pärnumaa
# 9 – Läänemaa, Hiiumaa, Saaremaa

# Kirjuta programm, mis kontrollib sisestatud indeksit (tähemärkide arv, vastav andmetüüp jne) ja näitab, millisesse maakonda see kuulub.

indeksid = ["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve", "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa", "Läänemaa, Hiiumaa, Saaremaa"]

while 1:
	try:
		postiindeks = int(input("Sisesta indeks: "))
		
		if len(str(postiindeks)) == 5:
			break
		else:
			print("On vaja 5 sümbolit")
			
	except:
		print("!!!")
		
print("Postiindeksi analuus")
indeks_list = list(str(postiindeks))
s1 = int(indeks_list[0])

print(f"Postiindeks {postiindeks} on {indeksid[s1-1]}")

##### Ülesanne 5 - Vahetus #####

# Напишите программу, которая меняет местами первый и последний элементы. (второй и предпоследний и т.д.). Количество меняемых местами элементов надо спросить у пользователя. В исходном списке минимум 2 элемента.

element_list = []

n = int(input("Mitu elemedni soovid sisestada: "))
print()

for i in range(N):
	element = input("Sisesta element: ")
	element_list.appent(element)
	
print()
print(f"Sisestatud loetelu: \n{element_list}")
print()

while True:
	k = int(input("Mitu vahetust soovid teha: "))
	print()
	
	if len(element_list) > 2 and k > 0 and k <= len(element_list) // 2:
		for i in range(k):
			element_list[i], element_list[-(i+1)] = element_list[-(i+1)], element_list[i]
			break
		
		else:
			print("Kahjuks see ei ole võimalik")
			print()
			
print()
print()

##### Ülesanne 6 - Бесполезные числа #####

# Николай задумался о поиске «бесполезного» числа на основании списка.
# Суть оного в следующем: он берет произвольный список чисел, находит самое большое из них, а затем делит его на длину списка и заменяет его в списке результатом деления.
# Студент пока не придумал, где может пригодиться подобное значение, но ищет у вас помощи в реализации такой функции.

# arvud = []
# try:
#     N=int(input("Mitu arvu soovid sisestada? "))
#     print()
#     if N<=0:
#         print("Peab olema rohkem kui 0")
#         print()
#     else:
#         for i in range(N):
#             while True:
#                 try:
#                     arv=int(input(f"Sissesta arv {i+1}: "))
#                     arvud.append(arv)
#                     break
#                 except:
#                     print("Sisesta õige arv")
#         print()
#         print(f"Sisestatud arvud: \n{arvud}")
#         print()
#         maks=max(arvud)
#         print(f"Suurem arv on: {maks}")
#         jag=round(maks/len(arvud),2)
#         print(f"Jagatis on: {jag}")
#         print()
#         pos=arvud.index(maks)
#         arvud[pos]=jag
#         print(f"Uuendatud loetelu:\n{arvud}")
# except:
#     print("SIsesta õige arv")
#     print()
# print()
# print()