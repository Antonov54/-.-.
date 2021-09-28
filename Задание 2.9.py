# _*_ coding: utf-8 _*_
print('Введите количеств долек по вертикале')
n = int(input())
print('Введите количеств долек по горизонтале')
m = int(input())
print('Введите количество всего долек')
k = int(input())
k1 = 0
def F(n,m,k,k1):
  k1 = (n*m) / 2
  if (k1==k): 
    return 'Да'
  elif (k1!=k): return 'Нет'
print(F(n,m,k,k1))