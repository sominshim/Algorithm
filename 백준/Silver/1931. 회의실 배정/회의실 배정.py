# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()

# 회의 수
N = int(data[0])

# 회의 정보 입력
meetings = []
for i in range(1, N + 1):
    start, end = map(int, data[i].split())
    meetings.append((start, end))

# 회의를 종료 시간 기준으로 정렬 (종료 시간이 같으면 시작 시간 기준)
meetings.sort(key=lambda x: (x[1], x[0]))

# 그리디 알고리즘으로 최대 회의 개수 계산
count = 0
last_end_time = 0

for start, end in meetings:
    if start >= last_end_time:  # 겹치지 않는 경우
        count += 1
        last_end_time = end  # 현재 회의의 종료 시간 업데이트

# 결과 출력
print(count)
