# -- coding: utf-8 --

def until0Average():
    counter = 1
    sum = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        counter+=1
        sum += x
    print(sum / counter)

until0Average()