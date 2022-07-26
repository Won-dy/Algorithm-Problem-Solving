# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def solution(board, moves):  # 모든 케이스 더 빠름

    # 빈칸 제거
    new_board = [[] for _ in range(len(board))]
    col = 0
    for i in zip(*board):
        print(i)
        for j in i:
            if j > 0:
                new_board[col].append(j)
            else:
                continue
        col += 1

    answer = 0
    bucket = [0]  # 바구니
    for move in moves:
        try:
            now_pos = new_board[move - 1].pop(0)  # 현재 위치의 맨 위 인형
            if bucket[-1] == now_pos:  # 바구니에 같은 인형이 쌓이면
                bucket.pop()  # 터뜨리기
                answer += 2
            else:  # 다른 인형이면
                bucket.append(now_pos)  # 바구니에 담기
        except:  # 인형이 없다면
            continue

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))  # 4