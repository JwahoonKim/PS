word = input()
upp = word.upper()
dic = dict()
for i in upp:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)

if len(dic) == 1:
    print(dic[0][0])
elif dic[0][1] == dic[1][1]:
    print('?')
else:
    print(dic[0][0])