# Вычислить площадь квадрата
# В инпут ввести размер стороны квадрата. Если число не целое - использовать точку (прим: 5.3)

import math

def countAreaOFSquare(side):
    x = (float(side) * float(side))
    print("Площадь квадрата = ", math.ceil(x))     #  Округленеие вверх
    
countAreaOFSquare(input("Сторона квадрата = "))