# 깊이 우선 탐색
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [0] * (n+1)
visited[0] = 1 # 인덱스 0은 고려하지 않음
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS
stack = []
start_node = list(graph.keys())[0]
stack.append(start_node)
visited[start_node] = 1 
connect_cnt = 1 # 연결요소 개수

while visited.count(0) > 0:
    if len(stack) == 0:
        connect_cnt += 1
        try:
            new_node = visited.index(0)
            stack.append(new_node)
            visited[new_node] = 1
        except:
            break
    node = stack.pop()
    for u in graph[node]:
        if visited[u] == 1:
            continue
        stack.append(u)
        visited[u] = 1

print(connect_cnt)
