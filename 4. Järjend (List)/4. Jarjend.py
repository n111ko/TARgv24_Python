# https://moodle.edu.ee/mod/assign/view.php?id=1340182

spisok = [] # empty array

numbers = [1, 2, 3, 4, 5]
abc = ['a', 'b', 'c']

word = "Programmeerimine"

word_list = list(word)

print(word)
print(word_list)

while True:
	print("1 - Добавь букву в список")
	print("2 - Соединить списки")
	print("3 - Добавить букву на i-позицию")
	print("4 - Удалить элемент из списка")
	choice = int(input())
	
	if choice == 1:
		a = input("Введи букву: ")
		word_list.append(a)
		print(f"Добавили {a} в список.", word_list)
	elif choice == 2:
		word_list.extend(abc)
		print(word_list)
	elif choice == 3:
		a = input("Введи букву: ")
		i = int(input("Введи номер позиции буквы в списке, куда добавить букву: "))
		word_list.insert(i-1, a) # 0, 1, 2
		print(word_list)
	elif choice == 4:
		a = input("Введи букву, которую хочешь удалить: ")
		n = word_list.count(a)
		
		if n > 0:
			for i in range(n):
				word_list.remove(a)
				
			print(word_list)
		else:
			print("Такой буквы нет.")