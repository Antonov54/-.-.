# _*_ coding: utf-8 _*_
print ('Введите количество секунд')
seconds=int(input())
days = seconds / 86400
hours = seconds / 3600
minutes = seconds / 60
print (days ,'дней:', hours ,'часов:', minutes ,'минут:', seconds ,'секунд')