def calculate_spacing(max_length, place, spacing, spacing_list):
    """
    입력 문자열에서 다음 문자로 넘어갈 때의 간격을 계산하는 함수.

    Parameters:
    - max_length (int): 최대 길이로 사용할 값
    - place (int): 이전 계산된 문자 간격
    - spacing: 문자열 자릿수
    - spacing_list (int_list): 반환할 리스트 업데이트

    Returns:
    - list: 각 문자와 다음 문자 간의 간격을 나타내는 리스트
    """
    spacing = max_length * spacing + 1
    spacing_list.insert(0, spacing) # list의 0번째 위치에 요소 추가 
    if place == 1: return spacing_list # 종료 조건

    return calculate_spacing(max_length, place - 1, spacing, spacing_list)

# 사용 예시:
# spacing_result = calculate_spacing(max_length=5, place=5, spacing=0, spacing_list=[])
# print(spacing_result)
def solution(word):
    vowels = {'A':0, 
              'E':1,
              'I':2,
              'O':3,
              'U':4}
    answer = 0

    spacing_result = calculate_spacing(max_length=5, place=5, spacing=0, spacing_list=[])
    for i in range(len(word)):
        answer += 1 + spacing_result[i] * vowels['{}'.format(word[i])]
        # print(word[i], answer)
    return answer