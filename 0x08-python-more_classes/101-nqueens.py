#!/usr/bin/python3
def SolveQueen(n):
    col = set()
    pD = set()
    nD = set()

    res = []

    board = [["."] * n for i in range(n)]
    print(board)

    def BackTrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in pD or (r - c) in nD:
                continue
            col.add(c)
            pD.add(r + c)
            nD.add(r - c)
            board[r][c] = "Q"
            
            BackTrack(r + 1)

            col.remove(c)
            pD.remove(r + c)
            nD.remove(r - c)
            board[r][c] = "."
    BackTrack(0)
    filtered = [s for s in res if any(c != '.' for row in s for c in row)]
    print(filtered)

SolveQueen(4)