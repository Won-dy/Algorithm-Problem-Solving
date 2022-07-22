# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    info = dict()  # 유저 아이디: 닉네임
    message = []
    for rcd in record:
        act = rcd.split()[0]
        uid = rcd.split()[1]

        if act == 'Leave':  # 채팅방 퇴장
            message.append([uid, '님이 나갔습니다.'])
        else:
            info[uid] = rcd.split()[2]  # 유저 아이디의 닉네임 저장
            if act == 'Enter': message.append([uid, '님이 들어왔습니다.'])  # 채팅방 입장

    answer = []
    for msg in message:
        answer.append(info[msg[0]] + msg[1])  # 유저 아이디에 맞는 닉네임 넣어 기록

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]