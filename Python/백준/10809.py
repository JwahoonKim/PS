alp_list = [-1] * 26
string = input()
for i in range(len(string)):
    if alp_list[ord(string[i]) - 97] == -1:
        alp_list[ord(string[i]) - 97] = i
for i in alp_list:
    print(i, end = ' ') 