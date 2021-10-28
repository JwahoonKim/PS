ja = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
      'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y' 'z']
mo = ['a', 'e', 'i', 'o', 'u']


def is_contain_mo(passwd):   # 모음 유무 체크
    for c in passwd:
        if c in mo:
            return True
    return False


def has_three_continue_mo_or_ja(passwd):   # 3개 연속 모음 자음 체크
    for i in range(len(passwd) - 2):
        cur = passwd[i:i+3]
        first_char_type = mo if cur[0] in mo else ja
        if cur[1] in first_char_type and cur[2] in first_char_type:
            return True
    return False


def has_double_char(passwd):  # 2개 연속 같은 글자
    for i in range(len(passwd) - 1):
        cur = passwd[i]
        next = passwd[i + 1]
        if cur == next and cur != 'e' and cur != 'o':
            return True
    return False


def is_valid_passwd(passwd):
    if is_contain_mo(passwd) and not has_three_continue_mo_or_ja(passwd) and not has_double_char(passwd):
        return True
    return False


while(1):
    passwd = input()
    if passwd == 'end':
        break
    if is_valid_passwd(passwd):
        print(f'<{passwd}> is acceptable.')
    else:
        print(f'<{passwd}> is not acceptable.')
