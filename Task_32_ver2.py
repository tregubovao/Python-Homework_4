# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.  2 2 3 5

n = (input('Задайте список чисел (через пробел): \n').split())
m = sorted([int(item) for item in n])
uniq_el = []
for el in m:
    count = 0
    for i in m:
        if el == i:
            count +=1
    if count > 1:                           
        continue
    else:
        uniq_el.append(el) 
print(uniq_el)