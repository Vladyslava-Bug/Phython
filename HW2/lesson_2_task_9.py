var_1 = 37
var_2 = 99

# 2й вариант (буферная переменная)
buf = var_1
var_1 = var_2
var_2 = buf

print("Var_1: ", var_1)
print("Var_2: ", var_2)

# 2й вариант (перезапись переменной)
# var_1 = 99
# var_2 = 37

# print("Var_1: ", var_1)
# print("Var_2: ", var_2)