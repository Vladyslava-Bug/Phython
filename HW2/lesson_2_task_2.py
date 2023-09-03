# Через инпут в переменную year задаем год, который хотим проверить. True - высокосный, False - нет.

year = input("Check year: ")

def is_year_leap(year):
    if (int(year) % 4 == 0):
        return (True)
    else: 
        return (False)

checkYear = is_year_leap(year)

answer = f"Year {year}: {checkYear}!!!" 
print(answer)