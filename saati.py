import numpy as np
while True:
    try:
        kolichestvo_criteriev = int(input("Введите количество критериев: "))
        break
    except ValueError:
        print('Введите число, а не буквы.')
matrica_sravneniy = np.eye(kolichestvo_criteriev) #создана матрица по количеству критериев
schetchik = 1  #для пропуска уже заполненных
for i in range(schetchik, kolichestvo_criteriev+1):
    for j in range(schetchik+1, kolichestvo_criteriev+1):
        while True:
            try:
                matrica_sravneniy[i-1][j-1] = round(float(input('Введите сравнение критерия {0} с критерием {1}: '.format(i, j))), 3) #наполнение
                break
            except ValueError:
                print('Введите число, а не буквы.')
        matrica_sravneniy[j-1][i-1] = round(matrica_sravneniy[i-1][j-1]**(-1), 2) #обратное наполнение
    schetchik += 1
comp_list = [round(sum(j),2) for j in matrica_sravneniy] #сумма коэффициентов
out_list = [round(n/sum(comp_list), 2) for n in comp_list]
if (sum(out_list)) != 1.0: #проверка на сумма коэффициентов = 1 и исправление если не сошлось
    index = out_list.index(max(out_list))
    k = (sum(out_list)) - 1.0
    out_list[index] -= k
print('Полученные весовые коэффициенты: ')
for znacheniya in out_list:
    print(znacheniya, end='   ')