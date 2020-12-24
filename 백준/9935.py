import sys
input = sys.stdin.readline

text = input().strip()
boom = input().strip()

while(True):
    # text가 아무것도 없어졌을때
    if text == '':
        text = 'FRULA'
        break
    # text에 더이상 boom 단어가 없을때
    if boom not in text:
        break
    # text에 boom 단어가 있을 때
    if boom in text:
        text = text.replace(boom, '')

print(text)