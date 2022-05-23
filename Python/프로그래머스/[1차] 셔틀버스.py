def timeToMinute(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m

def minuteToTime(minute):
    time = ''
    h, m = divmod(minute, 60)
    time += str(h) if h >= 10 else '0' + str(h)
    time += ':'
    time += str(m) if m >= 10 else '0' + str(m)
    return time

def solution(n, t, m, timetable):
    timeDict = dict()
    busTime = [timeToMinute("9:00") + i * t for i in range(n)]
    timetable.sort(reverse=True)

    for time in busTime:
        timeDict[time] = []
    
    for _ in range(n * m):
        if not timetable:
            break 
        person = timeToMinute(timetable.pop())
        for time in busTime:
            if (person <= time) and len(timeDict[time]) < m:
                timeDict[time].append(person)
                break

    if len(timeDict[busTime[-1]]) < m:
        return minuteToTime(busTime[-1])
    return minuteToTime(timeDict[busTime[-1]][-1] - 1)
