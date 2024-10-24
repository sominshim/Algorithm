from collections import deque

def minimum_time(N, tasks):
    # 그래프와 진입 차수를 저장할 리스트 초기화
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    time = [0] * (N + 1)
    dp = [0] * (N + 1)  # 각 작업을 완료하는 데 걸리는 최소 시간

    # 작업 정보 입력
    for i in range(1, N + 1):
        data = tasks[i - 1]
        time[i] = data[0]  # 해당 작업의 걸리는 시간
        in_degree[i] = data[1]  # 선행 관계의 개수
        for prerequisite in data[2:]:
            graph[prerequisite].append(i)

    # 진입 차수가 0인 작업들을 큐에 추가
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            dp[i] = time[i]  # 선행 작업이 없으면 자신의 시간이 최소 시간

    # 위상 정렬을 이용한 최소 시간 계산
    while queue:
        current = queue.popleft()
        for next_task in graph[current]:
            in_degree[next_task] -= 1
            # 다음 작업의 최소 시간 갱신
            dp[next_task] = max(dp[next_task], dp[current] + time[next_task])
            if in_degree[next_task] == 0:
                queue.append(next_task)

    # 모든 작업을 완료하는 데 걸리는 최소 시간
    return max(dp)

# 입력 처리 예시
N = int(input())  # 작업의 수
tasks = [list(map(int, input().split())) for _ in range(N)]

# 함수 호출 및 출력
print(minimum_time(N, tasks))
