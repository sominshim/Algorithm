def solution(triangle):
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i+1])):
            if j == 0:
                triangle[i+1][j] += triangle[i][j]
            elif j == i+1:
                triangle[i+1][j] += triangle[i][j-1]
            else:
                triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
    return max(triangle[-1])


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle)) # 30