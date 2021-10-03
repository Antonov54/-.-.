# _*_ coding: utf-8 _*_
print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
print('Введите третье число')
c = int(input())
def F(a,b,c):
  if ((a == b) and (a == c)):
    return '3'
  elif (a == b) or (a == c) or (b == c): 
    return '2'
  else: return '0'
print (F(a,b,c))