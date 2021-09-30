# _*_ coding: utf-8 _*_
print('Введите натуральное число')
n = int(input())
def F(n):
  if ((n % 4 ==0) and (n % 100 !=0)) or (n % 400 ==0):
    return'Да, год', n ,'високосный'
  else: return'Нет, год', n ,'не високосный'
print(F(n))