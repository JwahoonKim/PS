def solution(s):
    num_arr = []
    now = []
    answer = []
    num = ""
    s = s[1:-1]
    for i in s:
        if i == '{':
            num = ""
            now = []
        elif i.isdigit():
            num += i
        elif i == ',':
            now.append(int(num))
            num = ""
        elif i == '}':
            now.append(int(num))
            num_arr.append(now)
            now = []
    num_arr.sort(key=lambda x: len(x))
    for numbers in num_arr:
        for num in numbers:
            if num not in answer:
                answer.append(num)
    return answer
