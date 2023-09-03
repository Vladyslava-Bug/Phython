# Вычислить размер вклада (х) после (у) лет при условии +10% годовых.

def bank(x, y):
    sum = x
    for i in range(0, y):
        sum += sum * 0.1
        print("Your deposit amount after", [i + 1], "years is: ", sum)

bank(1000, 5)