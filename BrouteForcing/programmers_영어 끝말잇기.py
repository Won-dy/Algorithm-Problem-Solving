# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    for i in range(len(words) - 1):
        now_word = words[i]  # 현재 단어
        next_word = words[i + 1]  # 다음 단어
        if next_word in words[:i + 1] or now_word[-1] != next_word[0]:  # 다음 단어가 이미 말한 적 있는 단어이거나 끝말잇기 규칙을 틀리면
            return [(i + 1) % n + 1, (i + 1) // n + 1]
    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))  # [3,3]
print(solution(5, [
    "hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure",
    "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))  # [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))  # [1,3]