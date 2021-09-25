import field, ai, random

f = field.field(5, 3)
solver = ai.saper_solver(f)
res = solver.solve()
print(res)

win = 0
fall = 0

for _ in range(100):
    n = random.randint(3, 10)
    bombs_num = int(n * 0.1)
    f = field.field(n, bombs_num)
    solver = ai.saper_solver(f)
    res = solver.solve()
    if res == 'win':
        win += 1
    else:
        fall += 1

print(win, fall)