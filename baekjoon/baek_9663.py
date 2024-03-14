from pprint import pprint

n = 5


for row in range(n):
    for col in range(n):
        # 판 생성
        board = [[0 for _ in range(n)] for _ in range(n)]
        # 핀위치
        board[row][col] = 2
        # 핀위치의 가로에 전부 1 넣기
        board[row][0:] = [1 for _ in range(n)]
        # 핀위치의 세로에 전부 1 넣기
        # 핀위치
        board[row][col] = 2
        pprint(board)
