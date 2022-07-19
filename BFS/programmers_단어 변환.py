# https://programmers.co.kr/learn/courses/30/lessons/43163

def solution(begin, target, words):
    # 다른 알파벳이 1개인지 판별
    def is_diff_one(word1, word2):
        diff_cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff_cnt += 1
                if diff_cnt > 1:
                    return False
        return True

    visited = [False] * len(words)  # 방문 여부

    stack = [(begin, 0)]
    while stack:
        now_word, depth = stack.pop()

        if now_word == target:
            return depth

        for idx, word in enumerate(words):
            if visited[idx]:  # 방문했던 단어이면 무시
                continue

            if is_diff_one(now_word, word):  # 한글자 차이면
                stack.append((word, depth + 1))  # stack에 삽입
                visited[idx] = True  # 방문표시

    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0