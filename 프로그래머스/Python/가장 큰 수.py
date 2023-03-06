def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: str(x) * 3, reverse=True)
    return str(int(''.join(numbers)))
