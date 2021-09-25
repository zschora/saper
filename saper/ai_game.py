import field, ai, random

# тестовый запуск
f = field.field(5, 3)
solver = ai.saper_solver(f)
res = solver.solve()
print(res)

#запустим алгоритм сто раз, подсчитаем статистику
win = 0
fall = 0

for _ in range(100):
    n = random.randint(3, 10)
    bombs_num = int(n * n * 0.2)
    f = field.field(n, bombs_num) # поле, в 20% клеток - бомбы
    solver = ai.saper_solver(f)
    res = solver.solve()
    if res == 'win':
        win += 1
    else:
        fall += 1

print('win:', win, 'falls:', fall)