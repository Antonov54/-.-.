# _*_ coding: utf-8 _*_
print('Введите первое число')
a = int(input())
print('Введите второе число')
b = int(input())
print('Введите третье число')
c = int(input())
def f(a,b,c):
  if (a < c) and (a < b):
    return a
  elif b < c: return b
  else: return c
print(f(a,b,c))