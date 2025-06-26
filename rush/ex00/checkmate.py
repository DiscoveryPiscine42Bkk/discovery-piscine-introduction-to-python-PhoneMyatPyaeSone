#checkmate.py
def checkmate(board_str):
    board = board_str.strip().split("\n")
    size = len(board)

    board = [list(row) for row in board]

    king_pos = None
    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break

    if not king_pos:
        return

    def is_in_bounds(x, y):
        return 0 <= x < size and 0 <= y < size

    xk, yk = king_pos

    for dx, dy in [(1, -1), (1, 1)]:
        xp, yp = xk + dx, yk + dy
        if is_in_bounds(xp, yp) and board[xp][yp] == 'P':
            print("Success")
            return

    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x, y = xk + dx, yk + dy
        while is_in_bounds(x, y):
            piece = board[x][y]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break
            x += dx
            y += dy

    print("Fail")
