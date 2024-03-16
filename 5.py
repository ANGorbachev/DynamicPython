N, M = [int(x) for x in input().split()]

a = [[0] * M for _ in range(N)] # генерируем доску
a[0][0] = 1 # инициализируем положение коня

for i in range(1, N):  # Цикл для строк
    for j in range(1, M):  # Цикл для столбцов
        if j - 2 >= 0 and i - 2 >= 0:
            a[i][j] = a[i - 1][j - 2] + a[i - 2][j - 1]
        if j - 2 >= 0 and i - 2 < 0:
            a[i][j] = a[i - 1][j - 2]
        if j - 2 < 0 and i - 2 >= 0:
            a[i][j] = a[i - 2][j - 1]

print((a[-1][-1]))

