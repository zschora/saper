import field

def new_game():
    n, bombs_num = map(int, input('Введите ширину поля и кол-во бомб через пробел: ').split())
    f = field.field(n, bombs_num)
    game(f)

def load_game():
    f = field.field()
    f.load()
    print('Игровое поле:')
    f.print()
    game(f)

def game(f):
    while(f.check_win() != 'win' and f.check_win() != 'lose'):

        com = input()
        if com == 'Save':
            f.save()
            continue
        if com == 'Load':
            f.load()
            print('Игровое поле:')
            f.print()
            continue
        x, y, act = com.split()
        x, y = int(x), int(y)
        if act == 'Flag':
            f.set_flag(x, y)
        else:
            f.check(x, y)
        print('Игровое поле:')
        f.print()
        print(f.check_win())

com = input('Write "New" or "Load": ')

if com == "New":
    new_game()
elif com == "Load":
    load_game()