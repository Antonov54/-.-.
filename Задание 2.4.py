# _*_ coding: utf-8 _*_
def abc(a,b,l,n):
    return (n-1)*a+(n-2)*b+2*l
print('Горизонтальное растояние между дырочками')
a = int(input())
print('Вертикальное растояние между дырочками')
b = int(input())
print('Длинна свободного шнурка')
l = int(input())
print('количество дырочек')
n = int(input())
print('длинна всего шнурка')
print(abc(a,b,l,n))