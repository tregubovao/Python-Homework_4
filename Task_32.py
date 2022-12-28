# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.  2 2 3 5

n = (input('Задайте список чисел (через пробел): \n').split())
m = sorted([int(item) for item in n])
uniq_el = [] 
if len(m) == 1:
    uniq_el.append(m[0])
    print(uniq_el)
    exit()
if m[0] != m[1]:
    uniq_el.append(m[0])
for i in range(len(m) - 2):
    if (m[i] != m[i + 1] and m[i + 1] != m[i + 2]):
        uniq_el.append(m[i + 1]) 
if m[len(m) - 2] != m[len(m) - 1]:
    uniq_el.append(m[len(m) - 1])
print(uniq_el)
   