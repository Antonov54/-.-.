# -- coding: utf-8 --

def squareUp():
    i = 1
    N = int(input("Введите число - "))
    while i * i <= N:
        print(i * i)
        i+=1

squareUp()