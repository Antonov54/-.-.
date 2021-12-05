# -- coding: utf-8 --

def findDel():
    i = 2
    N = int(input("Введите число больше 2 - "))
    while N % i != 0:
        i += 1
    print(i)
findDel()