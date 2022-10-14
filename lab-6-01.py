import math as m
a = float(input("Введіть нижню границю: "))
b = float(input("Введіть верхню границю: "))
h = float(input("Введіть значення кроку: "))
spisok = []
spisokl = []
while a < b:
    levv = m.sin(a + m.pi) + m.cos(a + m.log(m.fabs(a)))
    spisok.append(a)
    spisokl.append(levv)
    a += h
spisok.append(spisokl)
print(spisok)
