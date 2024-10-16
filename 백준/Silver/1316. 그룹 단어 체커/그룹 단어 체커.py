# 그룹 단어인지 체크하는 함수
def is_group_word(word):
    seen = set()  # 이미 등장한 문자들을 저장할 집합
    prev_char = ''  # 이전에 등장한 문자

    for char in word:
        if char != prev_char:  # 현재 문자가 이전 문자와 다를 때
            if char in seen:  # 이미 등장한 문자라면 그룹 단어가 아님
                return False
            seen.add(char)  # 새로 등장한 문자를 추가
        prev_char = char  # 이전 문자를 현재 문자로 업데이트

    return True

# 입력 처리
n = int(input())
count = 0

# N개의 단어를 검사하여 그룹 단어인지 체크
for _ in range(n):
    word = input().strip()
    if is_group_word(word):
        count += 1

# 결과 출력
print(count)
