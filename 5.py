# Если вы были на Луне сейчас, ваш вес будет 16,5% от вашего веса
# земли. Для его расчета необходимо умножить на 0,165. Если в
# ближайшие 15 лет ваш вес будет увеличиваться на 1 кг каждый год.
# Какой будет ваш вес каждый год на Луне в следующие 15 лет?

n=1
age=int(input('Введите ваш вес:'))
agenow=age*0.165
print('вес на луне в 1 год='+str(agenow))
while n<15:
    age=age+1
    agenow=age*0.165
    n=n+1
    print('ваш вес на луне на '+str(n)+' год составит '+str(agenow))
