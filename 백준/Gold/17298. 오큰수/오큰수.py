n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n  # 오큰수를 저장할 리스트, 초기값은 -1로 설정
stack = []

# 스택을 이용해 오큰수를 찾음
for i in range(n):
    # 스택이 비어있지 않고, 현재 원소가 스택의 top 인덱스의 원소보다 클 때
    while stack and arr[stack[-1]] < arr[i]:
        index = stack.pop()
        ans[index] = arr[i]
    stack.append(i)

# 결과 출력
print(' '.join(map(str, ans)))
