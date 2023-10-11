from smartphone import Smartphone

catalog = [
    Smartphone("IPhone", "15", "+79441234567"),
    Smartphone("Samsung", "A53", "+79430000145"),
    Smartphone("Google", "Pixel 5", "+79345678901"),
    Smartphone("Huawei", "P40 Pro", "+79567890123"),
    Smartphone("iPhone", "12 Pro", "+79234567890")
]

for i in catalog:
    print(f'{i.brand} - {i.model}. {i.phone_number}')