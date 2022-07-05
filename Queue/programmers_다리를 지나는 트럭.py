# https://programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length, weight, truck_weights):
    answer = 0

    end_truck, bridge, wait_truck = [], [0] * bridge_length, truck_weights[:]

    sum_bridge_weight = 0  # 다리 위 트럭의 무게 합
    while len(end_truck) != len(truck_weights):

        answer += 1  # 시간 카운트

        # 다리에 있던 트럭들 1칸씩 앞으로 이동
        last_truck = bridge.pop(0)
        if last_truck != 0:  # 다리 끝에 트럭이 있으면
            end_truck.append(last_truck)  # 다리 끝에 있는 트럭은 다리를 다 지남
            sum_bridge_weight -= last_truck  # 다리 위 트럭 무게 갱신

        # 대기 트럭 있으면
        if wait_truck:
            # 현재 트럭 건너도 다리 최대 무게 넘지 않으면
            if sum_bridge_weight + wait_truck[0] <= weight:
                now_truck = wait_truck.pop(0)
                bridge.append(now_truck)  # 현재 순서 트럭 다리 건너기
                sum_bridge_weight += now_truck  # 다리 위 트럭 무게 갱신

            else:  # 최대 무게 넘으면
                bridge.append(0)  # 다리 길이 유지
        else:  # 대기 트럭 없으면
            bridge.append(0)  # 다리 길이 유지

    return answer


print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110