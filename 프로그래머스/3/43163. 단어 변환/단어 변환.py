from collections import deque, defaultdict
def solution(begin, target, words):
    n = len(begin) 
    q = deque([(begin, 0)])
    visited = set()

    while q:
        curr_word = q.popleft()
        if curr_word[0] == target:
            return curr_word[1]

        # begin과 알파벳이 1개 다른 단어 찾기
        for word in words:
            diff = 0
            for i in range(n):
                if curr_word[0][i] != word[i]:
                    diff += 1
                if diff > 1:
                    break
            # 알파벳이 1개만 다르고, 방문하지 않은 단어일 때,
            if diff == 1 and word not in visited:
                q.append((word, curr_word[1] + 1))
                visited.add(word)
            
    return 0


if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log"]
    
    print(solution(begin, target, words)) # 4