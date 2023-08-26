def get_num(num):
    return str(num) #str преобразовует формат num в string, что позволяет получить ответ без дополнительных пробелов между символами.

result = get_num(8) + get_num(8) + get_num(0) + get_num(0) + get_num(5) + get_num(5) + get_num(5) + get_num(3) + get_num(5) + get_num(3) + get_num(5)

print(result)