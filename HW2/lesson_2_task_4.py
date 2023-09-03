def fizz_buzz(num):
  for i in range(1,num):
    if (i % 3 == 0) and (i % 5 == 0):
      print("Fizzbuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif(i % 5 == 0):
      print("Buzz")
    else:
      print(i)


fizz_buzz(20)

#  Функция должна печатать числа от 1 до num. При этом:
#     1. если число делится на 3, печатать `Fizz`;
#     2. если число делится на 5, печатать `Buzz`;
#     3. если число делится на 3 и на 5, печатать `FizzBuzz`.