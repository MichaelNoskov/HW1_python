# Получаем данные пользователя (генератор списка, чтобы не повторять много раз input())
x1, y1, x2, y2 = [int(input()) for i in range(4)]
# Проверяем, находятся ли точки в одной половине относительно x и в одной относительно y: этого достаточно. Выводим "да"
if (x1 < 0) == (x2 < 0) and (y1 < 0) == (y2 < 0):
    print('YES')
# Иначе выводим "нет"
else:
    print('NO')