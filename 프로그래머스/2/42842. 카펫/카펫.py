def solution(brown, yellow):
    answer = []

    # brown 조합 찾기
    for i in range(3,brown-3):
        vertical = i
        horizon = int((brown+4)/2) - i
        if vertical*horizon == brown + yellow:
            return [horizon, vertical]

        if vertical == horizon:
            break

    return answer