def solution(m, n, board):
    board = list(map(lambda x: list(x), board))

    new_board = []

    for col in range(n):
        column = [board[row][col] for row in range(m - 1, 0 - 1, -1)]
        new_board.append(column)

    board = new_board

    count = 0

    while True:
        check_board = [[False for _ in range(len(board[col]))] for col in range(len(board))]

        for col in range(len(board)):
            for row in range(len(board[col])):

                # 맨 위, 맨 오른쪽인 경우는 제외
                if row == len(board[col]) - 1 or col == len(board) - 1:
                    continue

                # 오른쪽 위에 블럭이 있는지 확인
                if row + 1 >= len(board[col + 1]):
                    continue

                direct = [(0, 0), (0, 1), (1, 0), (1, 1)]
                # 4개의 블록이 모두 같은 경우
                if all([board[col + x][row + y] == board[col][row] for x, y in direct]):
                    # check_board에 표시
                    for x, y in direct:
                        check_board[col + x][row + y] = True

        # 제거할 블록이 없다면 break
        if not any([any(column) for column in check_board]):
            break

        # 제거할 블록이 있다면
        new_board = []
        for col in range(len(board)):
            column = []
            for row in range(len(board[col])):
                if check_board[col][row]:
                    count += 1
                else:
                    column.append(board[col][row])
            new_board.append(column)

        board = new_board

    return count
