import sys
input = sys.stdin.readline

start, end, str_end = map(str, input().split())

# 시간을 분으로 변환
min_start = int(start[0]) * 10 * 60 + int(start[1]) * 60 + int(start[3]) * 10 + int(start[4])
min_end = int(end[0]) * 10 * 60 + int(end[1]) * 60 + int(end[3]) * 10 + int(end[4])
min_str_end = int(str_end[0]) * 10 * 60 + int(str_end[1]) * 60 + int(str_end[3]) * 10 + int(str_end[4])

startPeople = set()
endPeople = set()

while(True):
    try:
        time, name = map(str, input().split())
        h, m = time.split(':')
        time = int(h) * 60 + int(m)
        if 0 <= time <= min_start:
            startPeople.add(name)
        elif min_end <= time <= min_str_end:
            endPeople.add(name)
    except:
        break
    
attendPeople = startPeople & endPeople
answer = len(attendPeople)

print(answer)