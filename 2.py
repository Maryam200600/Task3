# N учеников берут по K яблок и равномерно распределяют их между
# собой.оставшаяся (неделимая) часть остается в корзине. Сколько яблок
# каждый студент получит? Сколько яблок останется в корзине?
# Программа читает числа N и K. Она должна напечатать два ответа для
# вопросы выше. (Каждый ученик N возьмет K яблок и останется X))

apple=int(input('enter count apple:'))
n=int(input('enter count student:'))
k=apple//n
x=apple-(k*n)
print('each student will take '+str(k) + ' apples and '+str(x) + ' apples will remain')