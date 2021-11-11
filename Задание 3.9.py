# -- coding: utf-8 --
n = int(input())
f1 = 0
f2 = 1
for i in range (1, n+1):
  f_s = f1 + f2
  f1 = f2
  f2 = f_s
print(f_s)