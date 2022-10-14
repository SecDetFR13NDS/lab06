import math as m
a = int(input('Введіть нижню границю: '))
b = int(input('Введіть верхню границю: '))
h = int(input('Введіть значення кроку: '))
spisok = []
spisok1 = []
while a < b:
    lev = (m.sin(a + m.pi) + m.cos(a + m.log(m.fabs(a))))
    spisok.append(a)
    spisok1.append(lev)
    a = a+h
lev = 0
for bar in range(0, len(spisok1)):
    lev += spisok1[bar]
    spisok.extend(spisok1)
print(spisok)
print("Сумма значень функцій: " + str(lev))
