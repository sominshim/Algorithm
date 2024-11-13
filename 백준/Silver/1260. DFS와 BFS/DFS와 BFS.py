# 깊이 우선 탐색
import sys
input = sys.stdin.readline

# 입력 및 초기화
n, m, start_node = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n+1)

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS
stack = []
stack.append(start_node)
dfs = []

while len(stack) > 0:
    node = stack.pop()
    if visited[node] == True:
        continue
    visited[node] = True
    dfs.append(node)
    for u in sorted(graph[node], reverse=True): # 오름차순 순회
        if visited[u] == False:
            stack.append(u)

print(*dfs)

# BFS
from collections import deque
q = deque([start_node])
visited = [False] * (n+1)
bfs = []

while len(q) > 0:
    node = q.popleft()
    if visited[node] == True:
        continue

    bfs.append(node)
    visited[node] = True

    for u in sorted(graph[node]): # 내림차순 순회
        if visited[u] == False:
            q.append(u)

print(*bfs)