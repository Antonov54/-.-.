# -- coding: utf-8 --

def until0Bigger():
    counter = 0
    loopCount = 0
    while True:
        x = int(input("Введите число - "))
        if x == 0:
            break
        if(loopCount != 0):
            if(x > container):
                counter += 1
        container = x
        loopCount+=1
    print(counter)

until0Bigger()