# График данной функции - прямая. Следовательно, есть три случая его расположения относительно оси x:
# 1) Пересекает в одной точке
# 2) Лежит на ней
# 3) не пересекает (идёт параллельно ей)
a, b = int(input()), int(input())
# Второй случай бывает тогда, когда y не зависит от x (по нашему уравнению это тогда, когда a == 0). Также, если b
# будет != 0, то график функции сместиться и не будет иметь точек с y=0. Поэтому ax + b будет всегда == 0 только
# если a==b==0. Проверяем это:
if a == 0 and b == 0:
    print('INF')
# Также, как уже говорилось выше, ax + b не будет иметь пересечений с осью x, если он будет параллелен ей, что
# соблюдается только если a == 0 и b != 0
# (если а не ноль, то график станет наклонной и пересечётся с осью x (нас это не устраивает), а если же b будет == 0,
# то график будет являться осью x, что тоже нас не устраивает):
elif a == 0 or (b % a) != 0:
    # Именно в этом случае график не пересечётся с осью x
    print('NO')
# Остался третий случай, когда график пересечёт ось x в одной точке, и это будет при следующем x:
else:
    print(int(-b / a))