def solution(triangle):
    for i in range(len(triangle) - 1, 0, -1):
        # 왼쪽, 오른쪽 중 큰 값 저장
        max_bottom = []
        for j in range(len(triangle[i]) - 1):
            max_bottom.append(max(triangle[i][j],triangle[i][j + 1]))
        # up stage 에 더하기
        triangle[i - 1] = [x + y for x, y in zip(triangle[i - 1], max_bottom)]
        
    # print(triangle)
    return triangle[0][0]