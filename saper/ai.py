import field

class saper_solver():
    def __init__(self, f):
        self._f = f
        self._n = f._n
        self._ai_field = [[0 for _ in range(self._n)] for _ in range(self._n)]

    def solve(self, print_steps=False):
        while(self._f.check_win() != 'win' and self._f.check_win() != 'lose'):
            i, j = self._arg_min()

            bombs_neighbors = self._f.check(i, j)
            deltas = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1))
            for d1, d2 in deltas:
                if 0 <= i + d1 < self._n and 0 <= j + d2 < self._n:
                    self._ai_field[i+d1][j+d2] += 1
            if print_steps:
                (self._f.check_win())
        return self._f.check_win()

    def _arg_min(self):
        argmin = (0, 0)
        min = self._ai_field[argmin[0]][argmin[1]]
        for i in range(self._n):
            for j in range(self._n):
                if self._ai_field[i][j] < min:
                    min = ai_field[i][j]
                    argmin = (i, j)
        return argmin
