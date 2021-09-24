import field

f = field.field(3, 1)

while(f.check_win() != 'win' and f.check_win() != 'lose'):
    x, y, act = input().split()
    x, y = int(x), int(y)
    if act == 'Flag':
        f.set_flag(x, y)
    else:
        f.check(x, y)
    f.print()
    print(f.check_win())