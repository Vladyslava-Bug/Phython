#  Объявите класс User
class User:
 # 3. Объявите в классе конструктор.

    #Конструктор должен принимать на вход 2 параметра:
    #1. `first_name` — имя.
    #2. `last_name` — фамилия.

    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name  

##. Создайте в классе 3 метода, которые печатают:

    def sayMyName(self):                                      #    имя
       print("My name is", self.first_name)
    
    def sayMyLastName(self):                                  #   фамилию
       print("My last name is", self.last_name)

    def saymyFullnmae(self):                                  #   имя и фамилию
       print(f"My full name is {self.first_name} {self.last_name}! chka-chka, {self.first_name} {self.last_name}!")
       
