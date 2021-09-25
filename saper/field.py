import random

class field:
    def __init__(self, n = 5, bombs_number=random.randint(2, 5)):
        
        self._n = n
        # поле с инфой о бомбах
        self._field = [[0 for _ in range(n)] for _ in range(n)]
        # поле с инфой об игре (об открытых клетках)
        self._game = [[0 for _ in range(n)] for _ in range(n)]
        self._not_open = n * n - bombs_number
        self._not_flagged = bombs_number # бомбы без флага + пустые клетки с флагами
        self._losing = False
        self._key = random.randint(1, 1000000)
        
        # расставим случайно бомбы
        for i in range(bombs_number):
            i1 = random.randint(0, n - 1)
            i2 = random.randint(0, n - 1)
            if self._field[i1][i2] != 0:
                i -= 1
                continue
            self._field[i1][i2] = -1
        
        # подсчитаем кол-во бомб-соседей для пустых клеток
        deltas = ((0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1))
        for i1 in range(n):
            for i2 in range(n):
                if self._field[i1][i2] != -1:
                    continue
                for d1, d2 in deltas:
                    if n - 1 >= i1 + d1 >= 0 and n - 1 >= i2 + d2 >= 0:
                        if self._field[i1 + d1][i2 + d2] == -1:
                            continue
                        self._field[i1 + d1][i2 + d2] += 1

    def check(self, i1, i2): # ход, открытие клетки (i1, i2)
        current = self._field[i1][i2]
        if current == -1: # бомба, проигрыш
            self._losing = True
        else:
            self._not_flagged -= 1 if self._game[i1][i2] == 2 else 0
            self._not_open -= 1

        self._game[i1][i2] = 1
        return self._field[i1][i2]

    def get_bombs_num(self, i1, i2):
        return self._field[i1][i2]

    def set_flag(self, i1, i2):
        self._game[i1][i2] = 2
        if self._field[i1][i2] == -1:
            self._not_flagged -= 1
        else:
            self._not_flagged += 1

    def print(self):
        for i1 in range(len(self._field)):
            for i2 in range(len(self._field)):
                if self._game[i1][i2] == 0:
                    print('-', end=' ')
                if self._game[i1][i2] == 2:
                    print('f', end=' ')
                if self._game[i1][i2] == 1:
                    print(self._field[i1][i2], end=' ')
            print()

    def check_win(self):
        if self._losing:
            return 'lose'
        elif self._not_open == 0 or self._not_flagged == 0:
            return 'win'
        else:
            return 'not the end'

    def save(self):
        f = open('data', 'w')
        
        random.seed(self._key)
        f.write(str(self._key) + ' ')
        f.write(str(self._not_open + random.randint(0, 100)) + ' ')
        f.write(str(self._not_flagged + random.randint(0, 100)) + ' ')
        f.write(str(int(self._losing + random.randint(0, 100))) + ' ')
        f.write(str(self._n + random.randint(0, 100)) + ' ')
        f.write('\n')

        for line in self._field:
            for el in line:
                f.write(str(el + random.randint(0, 100)) + ' ')
            f.write('\n')

        for line in self._game:
            for el in line:
                f.write(str(el + random.randint(0, 100)) + ' ')
            f.write('\n')
        f.close()

    def load(self):
        f = open('data', 'r')
        
        file = f.readlines()
        f.close
        val = list(map(int, file[0].split()))
        self._key = int(val[0])

        random.seed(self._key)
        self._not_open = int(val[1]) - random.randint(0, 100)
        self._not_flagged = int(val[2]) - random.randint(0, 100)
        self._losing = int(val[3]) - random.randint(0, 100)
        self._n = int(val[4]) - random.randint(0, 100)
        
        self._field = [[0 for _ in range(self._n)] for _ in range(self._n)]
        self._game = [[0 for _ in range(self._n)] for _ in range(self._n)]

        for i in range(self._n):
            line = list(map(lambda x: int(x) - random.randint(0, 100), file[i+1].split()))
            self._field[i] = line

        for i in range(self._n):
            line = list(map(lambda x: int(x) - random.randint(0, 100), file[self._n+i+1].split()))
            self._game[i] = line
