# _*_ coding: utf-8 _*_
def F():
  a1 = int(input())
  a2 = int(input())
  b1 = int(input())
  b2 = int(input())
  if((1 <= a1 <= 8) and (1 <= a2 <= 8) and (1 <= b1 <= 8) and (1 <= b2 <= 8)):
        if(((a1 % 2 != 0) and (a2 % 2 != 0)) or ((a1 % 2 == 0) and (a2 % 2 == 0))):
            fC = "Чёрный"
        else:
            fC = "Белый"
        if(((b1 % 2 != 0) and (b2 % 2 != 0)) or ((b1 % 2 == 0) and (b2 % 2 == 0))):
            sC = "Чёрный"
        else:
            sC = "Белый"
        if(sC == fC):
            return "Да"
        else:
            return "Нет"
print(F())