from datetime import *
from calendar import *
from math import *


def summa3(arv1:int, arv2:int, arv3:int)->int:
    """Tagastab kolme täisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int

    """

    summa = arv1 + arv2 + arv3
    return summa



#1
def arithmetic(a:float, b:float, arg:str):
    """

    :param float arg1: Esimene number
    :param float arg2: Teine number
    :param str arg3: Argument

    """

    if arg == "+":
        c = a + b
    elif arg == "-":
        c = a - b
    elif arg == "*":
        c = a * b
    elif arg == "/":
        c = a / b

    return c



#2
def is_year_leap(aasta:int) -> bool:
    """
    """

    if aasta % 4 == 0:
        v = True

    else:
        v = False

    return v


#3
def square(a:float):
    """

    :param float a: Külje pikkus

    """

    P = round(4 * a, 2)
    S = round(a * a, 2)
    d = round(sqrt((a * a) + (a * a)), 2)

    return P, S, d



#4
def season(arg:int):
    """

    :param int arg: kuu number

    """

    if arg <= 2 or arg == 12:
        print("Talv")
    elif arg <= 5:
        print("Kevad")
    elif arg <= 8:
        print("Suvi")
    elif arg <= 11:
        print("Sügis")

    return arg



#5
# каждый год a увеличивается на 10% --> прибавляется к сумме вклада --> заново
def bank(a:float, years:int):
    """

    :param float a: euro
    :param int year: aasta

    """

    for _ in range(years):
        a *= 1.1
        # 0.1 - 10% от суммы
        # 1.1 - сумма(1) + 10% от суммы(0.1)

    return a



#6
def is_prime(arg:int) -> bool:
    """

    :param int arg: argument

    """

    if arg <= 1:
        return False
    for i in range(2, int(sqrt(arg)) + 1):
        if arg % i == 0:
            return False
    return True



#7
def date(p, k, a):
    """

    :param int p: päev
    :param int k: kuu
    :param int a: aasta

    """