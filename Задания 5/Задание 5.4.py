# -- coding: utf-8 --

def sport():
    x = int(input("Введите первое число - "))
    y = int(input("Введите второе число - "))
    counter = 1
    while x < y:
        x *= 1.1
        counter+=1
    print(counter)
sport()