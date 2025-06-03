inventory = []
chest = ['boots', 'sword', 'sock', 'carrot']

while True:
	print("1 - Открыть инвентарь")
	print("2 - Добавить предмет")
	print("3 - Удалить предмет")
	print("4 - Очистить инвентарь")
	print("5 - Открыть этот подозрительный сундук")
	print("6 - Закрыть инвентарь")
	
	while True:
		try:
			print("----------------")
			choice = int(input("Что ты хочешь сделать? (1-6) "))
			print("----------------")
			print()
			break
		except:
			print()
			print("----------------")
			print("Необходимо выбрать значение от 1 до 6.")
			print("----------------")
			print()
			
	if choice == 1:
		if len(inventory) == 0: # or inventory == []
			print()
			print("----------------")
			print("Здесь пусто.")
			print("----------------")
			print()
			
		else:
			print()
			print("----------------")
			print(inventory)
			print("----------------")
			print()
			
	elif choice == 2:
		print()
		print("----------------")
		item = input("Введи название предмета, который ты хочешь получить: ")
		print("----------------")
		print()
		inventory.append(item)
		
	elif choice == 3:
		print()
		print("----------------")
		item = input("Введи название предмета, который ты хочешь удалить: ")
		print("----------------")
		print()
		inventory.remove(item)
		
	elif choice == 4:
		while True:
			try:
				print()
				print("----------------")
				question = input("Ты уверен/а, что хочешь очистить инвентарь? y/n")
				print("----------------")
				print()
				
				if question == "y":
					inventory.clear()
					print()
					print("----------------")
					print("Инвентарь очищен.")
					print("----------------")
					print()
					break
				elif question == "n":
					print()
					print("----------------")
					print("Инвентарь не будет очищен.")
					print("----------------")
					print()
					break
			
			except:
				print()
				print("----------------")
				print("Необходимо выбрать y/n.")
				print("----------------")
				print()
				
	elif choice == 5:
		print()
		print("----------------")
		print("Ты открыл/а подозрительный сундук. В твоем инвентаре появились новые вещи.")
		print("----------------")
		print()
		print("----------------")
		print(inventory)
		print("----------------")
		print()
		print("----------------")
		inventory.extend(chest)
		print(chest)
		print("----------------")
		print()
	elif choice == 6:
		print("До встречи.")
		break