import random

class field:
    def __init__(self, n, bombs_number=random.randint(2, 5)):
        # -1 - бомаба
        self._field = [[0 for _ in range(n)] for _ in range(n)]
        self._game = [[0 for _ in range(n)] for _ in range(n)]
        self._not_open = n * n - bombs_number
        self._losing = False
        
        for i in range(bombs_number):
            i1 = random.randint(0, n - 1)
            i2 = random.randint(0, n - 1)
            if self._field[i1][i2] != 0:
                i -= 1
                continue
            self._field[i1][i2] = -1
        
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

    def check(self, i1, i2):
        current = self._field[i1][i2]
        self._game[i1][i2] = 1
        if current == -1:
            self._losing = True
        else:
            self._not_open -= 1

    def get_bombs_num(self, i1, i2):
        return self._field[i1][i2]

    def set_flag(self, i1, i2):
        self._game[i1][i2] = 2

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
        elif self._not_open == 0:
            return 'win'
        else:
            return 'not the end'