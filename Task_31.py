

n = int(input('Введите произвольное целое число: \n')) 
prost_mnozh = []
for i in range(2, n):
    if n % i == 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prost_mnozh.append(i)
if len(prost_mnozh) == 0:
    print('Данное число не имеет простых множителей')
else:
    print(f'Простые множители числа {n}: {prost_mnozh}')
        
        