for case in range(1, 11):
    n = int(input())
    board = []
    for i in range(8):
        board.append(input())

    total = 0
    # 가로 글자 찾기
    for i in board:
        for j in range(len(i) - n + 1):
            n_text = i[j:n + j]
            if n_text == n_text[::-1]:
                total += 1

    # 세로 글자 찾기
    for i in range(len(board)):
        col = ""
        for j in board:
            col += j[i:i+1]
        for l in range(len(col) - n + 1):
            n_col = col[l:n + l]
            if n_col == n_col[::-1]:
                total += 1
    print(f'#{case} {total}')

