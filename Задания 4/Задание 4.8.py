# -- coding: utf-8 --
s = input()
sB = s[:s.find('h')]
sM = s[int(s.find('h')):int(s.rfind('h') + 1)]
sA = s[s.rfind('h') + 1:]
print(sB + sM[::-1] + sA)