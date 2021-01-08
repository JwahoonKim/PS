
def isCommon(str1, str2):
    cursor = 0
    if len(str1) > len(str2):
        return 0
    for i in str1:
        a = str2.find(i, cursor)
        if a == -1:
            return 0
        else:
            cursor = a + 1
    return len(str1)

a = 'abc'
b = 'abcde'
print(isCommon(a,b))