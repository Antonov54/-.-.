# -- coding: utf-8 --
s = input()
x = int(s.find(' ')) +1
z = int(len(s))
f = str(s[x:z]) + str(' ') + str(s[:x])
print(f)