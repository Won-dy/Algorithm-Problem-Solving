# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    # 해시 만들기
    musics = dict()  # 장르: (재생 횟수, 고유 번호)
    plays_cnt_dic = dict()  # 장르: 총 재생 횟수
    for num, genre, play in zip([n for n in range(len(plays))], genres, plays):
        if genre in musics:
            musics[genre] += [(play, num)]
            plays_cnt_dic[genre] += play
        else:
            musics[genre] = [(play, num)]
            plays_cnt_dic[genre] = play

    # 재생 횟수 기준 내림차순 정렬
    plays_cnt = sorted(plays_cnt_dic.items(), key=lambda x: x[1], reverse=True)

    # 재생횟수 오름차순 정렬 (고유 번호는 이미 내림차순)
    for genre, play in musics.items():
        musics[genre] = sorted(play, key=lambda x: x[0], reverse=True)

    answer = []
    for pc in plays_cnt:
        answer.append(musics[pc[0]][0][1])
        try:
            answer.append(musics[pc[0]][1][1])
        except IndexError:
            pass

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]