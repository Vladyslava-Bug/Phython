def month_to_season(mon):
    mon = int(mon)
    if (mon == 1) or (mon == 2) or (mon == 12):
        print("Winter")
    elif (mon == 3) or (mon == 4) or (mon == 5):
        print("Spring")
    elif (mon == 6) or (mon == 7) or (mon == 8):
        print("Summer")
    elif (mon == 9) or (mon == 10) or (mon == 11):
        print("Autumn")
    else:
        print("It's not a month")

month_to_season(input("Numer of month: "))


# Функция выводит сезон к которыму принадлежит порядковый номер месяца (mon).
# Дополнительно реализован вывод названия месяца следующим кодом (вставить 2й и 3й строкой):

# m = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август" "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

# print(m[mon -1])