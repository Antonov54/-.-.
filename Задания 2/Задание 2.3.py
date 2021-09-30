# _*_ coding: utf-8 _*_
print('Введите число минут')
n=int(input())
n=n%(24*60)
m=n%60
c=n//60
print(c,'часов',m, 'минут')