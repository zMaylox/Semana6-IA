def free(row, col):
    """ Determina si la casilla rowxcol está libre de ataques.
    @param row: Fila
    @param col: Columna
    @return: True si la casilla está libre de ataques por otras reinas.
    """
    for i in range(8):
        if tablero[row][i] == 'R' or tablero[i][col] == 'R':
            return False

    if row <= col:
        c = col - row
        r = 0
    else:
        r = row - col
        c = 0
    while c < 8 and r < 8:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c += 1

    if row <= col:
        r = 0
        c = col + row
        if c > 7:
            r = c - 7
            c = 7
    else:
        c = 7
        r = row - (7 - col)

    while c >= 0 and r < 8:
        if tablero[r][c] == 'R':
            return False
        r += 1
        c -= 1

    return True


def agregar_reina(n):
    """ Agrega n reinas al tablero.
    @param: n El número de reinas a agregar
    @return True si se pudo agregar las reinas requeridas
    """
    if n < 1:
        return True

    for idx_row in range(8):
        for idx_col in range(8):
            if free(idx_row, idx_col):
                tablero[idx_row][idx_col] = 'R'
                if agregar_reina(n - 1):
                    return True
                else:
                    tablero[idx_row][idx_col] = '_'

    return False


tablero = []
for i in range(8):
    tablero.append(['_'] * 8)
agregar_reina(8)
for row in tablero:
    print(*row)