# Вычислить число ПИ c заданной точностью d
# Пример:  при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
print(math.pi)
with open('data_30.txt', 'r', encoding='utf-8') as file:
    d = float(file.readline())
count = 0    
while d < 1:
    count += 1
    d *= 10
print(round(math.pi, count))   
