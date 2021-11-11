# -- coding: utf-8 --
s = input()
if s.count('f') == 1:
    print(s.find('f') + 1)
elif s.count('f') >= 2:
    print(s.find('f') +1, s.rfind('f') +1)