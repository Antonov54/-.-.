# -- coding: utf-8 --
k = int(input())
n = int(input())
f1 = 0
f2 = 1
z = k+n
for i in range (1, z+1):
  f_s = f1 + f2
  f1 = f2
  f2 = f_s
print(f_s)