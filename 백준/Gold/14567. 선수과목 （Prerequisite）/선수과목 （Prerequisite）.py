from collections import deque

def minimum_semesters(N, M, prerequisites):
    # 그래프와 진입 차수를 저장할 리스트 초기화
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    semester = [0] * (N + 1)  # 각 과목을 몇 학기에 들을 수 있는지 저장

    # 선수과목 관계 입력
    for a, b in prerequisites:
        graph[a].append(b)
        in_degree[b] += 1

    # 진입 차수가 0인 과목들을 큐에 추가 (첫 학기에 들을 수 있는 과목들)
    queue = deque()
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            queue.append(i)
            semester[i] = 1  # 진입 차수가 0이면 첫 학기에 들을 수 있음

    # 위상 정렬
    while queue:
        current = queue.popleft()
        for next_course in graph[current]:
            in_degree[next_course] -= 1
            # 선수과목을 이수한 후, 다음 과목을 이수할 수 있는 학기 갱신
            semester[next_course] = max(semester[next_course], semester[current] + 1)
            if in_degree[next_course] == 0:
                queue.append(next_course)

    # 결과 출력 (1번 과목부터 N번 과목까지)
    return " ".join(map(str, semester[1:]))

# 입력 처리
N, M = map(int, input().split())  # 과목 수, 선수 조건 수 입력
prerequisites = [tuple(map(int, input().split())) for _ in range(M)]

# 함수 호출 및 출력
print(minimum_semesters(N, M, prerequisites))
