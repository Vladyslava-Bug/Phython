lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# Вывести сумму всех элементов

sum = 0

for i in range(0, len(lst)):
    sum += lst[i]

print(sum)  

# 2й способ
# sum = 0
# for i in lst:
#     sum += i
# print("Total: ", sum)

# 3й способ
# sum = sum(lst)
# print(sum)