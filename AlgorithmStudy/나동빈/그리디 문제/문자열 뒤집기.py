# 전부 0으로 만드는 경우와 전부 1로 만드는 경우 중 최소값이 정답

data = input() 
count0 = 0
count1 = 0

if data[0] == '0':
    count1 += 1
else:
    count0 += 1 

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

answer = min(count0, count1)
print(answer)
