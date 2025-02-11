def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        prev_number = phone_book[i-1]
        if prev_number == phone_book[i][:len(prev_number)]:
            return False
    return True