# 입력 받기
N = int(input())
F = int(input())

# N의 마지막 두 자리를 00으로 변경한 값 구하기
new_N = (N // 100) * 100

# 00부터 99까지의 값을 확인하여 F로 나누어떨어지는 최소값 찾기
for i in range(100):
    if (new_N + i) % F == 0:
        # 두 자리로 만들어서 출력
        print(f'{i:02}')
        break