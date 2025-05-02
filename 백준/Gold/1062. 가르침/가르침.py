import sys
from itertools import combinations

def solution(n, k, words):
    """
    
    """
    if k < 5: # 필수 알파벳 만족 못함
        return 0
    
    essential = {'a', 'n', 't', 'i', 'c'}
    learned = essential.copy()
    new_words = [set(word[4:-4]) for word in words] # anta, tica 제거

    # 나머지 알파벳 후보
    all_letters = [chr(i + ord('a')) for i in range(26)]
    candidates = [ch for ch in all_letters if ch not in essential]

    # 후보 알파벳의 k-5개 조합
    comb_list = list(combinations(candidates, k - 5))
    max_count = 0

    # 조합 하나씩 탐색
    for i in range(len(comb_list)):
        for ch in comb_list[i]:
            learned.add(ch)
        
        # 읽을 수 있는 단어 개수 계산
        readable = 0
        for word in new_words:
            for ch in word:
                if ch not in learned:
                    break
            else:
                readable += 1
    
        max_count = max(max_count, readable)
        
        for ch in comb_list[i]: # 상태 복원
            learned.remove(ch)

    return max_count

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())

    words = []
    for _ in range(n):
        words.append(sys.stdin.readline().strip())
    
    print(solution(n, k, words))