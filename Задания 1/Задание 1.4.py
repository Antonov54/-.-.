# -*- coding: utf-8 -*-
print("Введите количество секунд:")
seconds = int(input())
days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 86400 % 3600 // 60
sec = seconds % 86400 % 3600 % 60
print (days,'Дней' ,hours,'Часов',minutes,'Минут',sec, 'Секунд')