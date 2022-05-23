import sys

input = sys.stdin.readline

def is_palindrome(str):
    return str == str[::-1]

def find_diff_index(str):
    for i in range(len(str) // 2):
        if str[i] != str[-i-1]:
            return i

def is_pseudo_palindrome(str):
    # str을 양 끝에서 비교해나가면서 palindrome 체크할 범위를 줄여나간다.
    diff_idx = find_diff_index(str)
    if diff_idx != 0:
        str = str[diff_idx : -diff_idx]
    return is_palindrome(str[1:]) or is_palindrome(str[:-1])
    
T = int(input())

for _ in range(T):
    str = input().rstrip()
    if is_palindrome(str):
        print(0)
    elif is_pseudo_palindrome(str):
        print(1)
    else:
        print(2)