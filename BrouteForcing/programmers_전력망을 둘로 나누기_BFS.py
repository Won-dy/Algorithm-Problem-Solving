# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque


def solution(n, wires):
    def bfs(node, visited):
        nonlocal cnt1

        queue = deque()
        queue.append(node)
        visited[node] = True  # 방문 처리
        cnt1 += 1  # 송전탑 개수 카운트

        while queue:
            now_node = queue.popleft()
            for next_node in tree[now_node]:  # 현재 송전탑과 연결되어 있는 송전탑 중
                if not visited[next_node]:  # 방문하지 않은 송전탑이면
                    queue.append(next_node)
                    cnt1 += 1  # 송전탑 개수 카운트
                    visited[next_node] = True  # 방문 처리

    answer = n

    # 전선 하나 끊어서 트리 만들기
    for cut in range(len(wires)):

        tree = [[] for _ in range(n + 1)]
        for idx, wire in enumerate(wires):
            if idx != cut:
                tree[wire[0]].append(wire[1])
                tree[wire[1]].append(wire[0])

        visited = [False] * (n + 1)
        cnt1 = 0
        # 연결된 송전탑 개수 구하기
        bfs(1, visited)

        answer = min(answer, abs(n - cnt1 * 2))  # 송전탑 개수의 차이가 최소면 갱신

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))  # 3
print(solution(4, [[1, 2], [2, 3], [3, 4]]))  # 0
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))  # 1