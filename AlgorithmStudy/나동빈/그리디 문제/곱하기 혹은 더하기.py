num_list = list(map(int, input()))
for i in range(1, len(num_list)):
    first = num_list[i - 1]
    second = num_list[i]
    if first <= 1 or second <= 1 :
        num_list[i] = first + second
    else:
        num_list[i] = first * second
print(num_list[-1])