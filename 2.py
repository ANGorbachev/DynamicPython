# Инициализация вводных данных
N = int(input())
m = [0] + [int(x) for x in input().split()]

# Рассчитаем максимально возможный вес гирь
M = sum(m)

# Для начала этот максимальный вес должен быть чётным числом
if M % 2 == 0:
    balance = M // 2
    # Далее применим стандартную задачу о рюкзаке, но для половинной массы:
    dp = [[False] * (balance + 1) for _ in range(N + 1)] # Инициализация массива возможности положить гирю (ДА/НЕТ) значениями False
    dp[0][0] = True # Нулевое значение сделаем True - ведь 0 можно положить)
    for i in range(1, N + 1): # Пробегаем по всем гирькам
        for j in range(0, balance + 1): # Пробегаем по всем значениям половинной массы
            dp[i][j] = dp[i - 1][j] # Присваиваем изначально предыдущему значению
            if m[i] <= j and dp[i - 1][j - m[i]]: # Если текущую гирю можно положить на весы (т.е. в клетке до того как положили гирю True)
                dp[i][j] = True # То обновляем текущую позицию в True потому что можно положить

    # Проверка True в последнем ряду, т.е. после проверки всех предметов (гирь)
    inds = []
    for j in range(balance + 1):
        if dp[N][j]:
            inds.append(j)

    # Если максимальный индекс соответствуем половинному весу, значит нам удалось собрать набор гирь, иначе - НЕТ.
    if max(inds) == balance:
        print(True)
    else:
        print(False)

else:
    print(False)

