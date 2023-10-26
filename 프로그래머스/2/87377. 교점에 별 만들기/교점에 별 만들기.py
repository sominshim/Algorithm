def solution(line):
    point = set()
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)

    # 1. 해를 구한다.
    for i in range(len(line)):
        a, b, e = line[i]
        for j in range(i+1, len(line)):
            c, d, f = line[j]
            # 해가 없을 경우 예외처리(평행)
            if a * d == b * c: continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)

            # 정수 확인 & 최대, 최소 x, y 좌표
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                point.add((x, y))

                if x_min > x: x_min=x
                if x_max < x: x_max=x
                if y_min > y: y_min=y
                if y_max < y: y_max=y

    # 2. 최대, 최소 x, y간의 거리를 구한다 -> 배열을 .으로 초기화한다
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    answer = [['.'] * x_len for _ in range(y_len)]

    # 3. 최솟값 x를 전체 교점에서 - 빼고, 최댓값 y를 전체 교점에서 -빼고 절댓값을 씌운다.
    # -> 계산된 교점을 *으로 바꾼다.
    for x, y in point:
        answer[int(abs(y-y_max))][int(x-x_min)] = '*'

    for i in range(len(answer)):
        answer[i]="".join(answer[i])

    # 4. 배열을 리턴한다.
    return answer