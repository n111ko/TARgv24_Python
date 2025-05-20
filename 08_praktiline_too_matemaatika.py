# Написать программу для проверки знаний по математике.

# Предложить пользователю выбрать сложность заданий.
# Например:

#     Tase 1, Tase 2, Tase 3
#     количество действий(+,-,/,*,**)
#     величину случайно генерируемых чисел.


# В программе случайным образом "задаются" примеры, с учетом сложности провряемых знаний.
# После введенного пользователем ответа, проверяется его правильностью.

# Придумать условие выхода из цикла.(можно сначала указать количество примеров)

# В конце работы программы, надо сообщить тестируемому оценку.
# <60% - Hinne 2
# 60-75% - Hinne 3
# 75-90% - Hinne 4
# >90% - Hinne 5

from random import *
while True:
    while True:
        try:
            tase = int(input("Vali ülesannete tase 1/2/3: "))
            print()

            if tase == 1 or tase == 2 or tase == 3:
                break
            else:
                print("On vaja sisestada number 1/2/3: ")
                print()

        except:
            print("On vaja sisestada number 1/2/3: ")


    if tase == 1:
        N = 5
        count = 0

        for i in range(N):
            a = randint(1,100)
            b = randint(1,100)
            operation = choice(["+", "-"])

            while True:
                try:
                    vastus = int(input(f"Ülesanne {i+1}\n{a}{operation}{b} = "))
                    break
                except:
                    print("Sisesta vastus: ")
                    print()
            if operation == "+":
                v = a + b
            elif operation == "-":
                v = a - b

            if vastus == v:
                print("Vastus on õige.")
                print()
                count += 1
            else:
                print("Vastus on vale.")
                print()
        tulemus = count * 100 / N

        if tulemus < 60:
            hinne = 2
        elif tulemus >= 60 and tulemus <= 74.99:
            hinne = 3
        elif tulemus >= 75 and tulemus <= 89.99:
            hinne = 4
        else:
            hinne = 5
        print(f"Sul on {count} õiget vastust. Sinu hinne on {hinne}")

    elif tase == 2:
        N = 10
        count = 0

        for i in range(N):
            a = randint(1,100)
            b = randint(1,100)
            operation = choice(["+", "-", "/", "*"])

            while True:
                try:
                    vastus = int(input(f"Ülesanne {i+1}\n{a}{operation}{b} = "))
                    break
                except:
                    print("Sisesta vastus: ")
                    print()
            if operation == "+":
                v = a + b
            elif operation == "-":
                v = a - b
            elif operation == "/":
                v = round((a / b), 0)
            elif operation == "*":
                v = a * b

            if vastus == v:
                print("Vastus on õige.")
                print()
                count += 1
            else:
                print("Vastus on vale.")
                print()
        tulemus = count * 100 / N

        if tulemus < 60:
            hinne = 2
        elif tulemus >= 60 and tulemus <= 74.99:
            hinne = 3
        elif tulemus >= 75 and tulemus <= 89.99:
            hinne = 4
        else:
            hinne = 5
        print(f"Sul on {count} õiget vastust. Sinu hinne on {hinne}")
    elif tase == 3:
        N = 15
        count = 0

        for i in range(N):
            a = randint(1,100)
            b = randint(1,100)
            operation = choice(["+", "-", "/", "*", "**"])

            while True:
                try:
                    vastus = int(input(f"Ülesanne {i+1}\n{a}{operation}{b} = "))
                    break
                except:
                    print("Sisesta vastus: ")
                    print()
            if operation == "+":
                v = a + b
            elif operation == "-":
                v = a - b
            elif operation == "/":
                v = round((a / b), 0)
            elif operation == "*":
                v = a * b
            elif operation == "**":
                v = a ** b

            if vastus == v:
                print("Vastus on õige.")
                print()
                count += 1
            else:
                print("Vastus on vale.")
                print()
        tulemus = count * 100 / N

        if tulemus < 60:
            hinne = 2
        elif tulemus >= 60 and tulemus <= 74.99:
            hinne = 3
        elif tulemus >= 75 and tulemus <= 89.99:
            hinne = 4
        else:
            hinne = 5
        print(f"Sul on {count} õiget vastust. Sinu hinne on {hinne}")