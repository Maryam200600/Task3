# Спросите пользователя написать строку и распечатайте, является ли
# эта строка палиндромом или нет. (Палиндром - это строка, которая
# читает одно и то же вперед и назад.)

polindrom=str(input('введите строку:'))
print(polindrom)
l=len(polindrom)
for i in range(l//2):
    if polindrom[i]!=polindrom[-1-i]:
        print('Данная строка не является палиндромом')
        quit()
print('Данная строка - палиндром!')