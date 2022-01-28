def getTime(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    time = (eh - sh) * 60 + (em - sm)
    return time

def getMusicArr(musicString, time):
    result = []
    for c in musicString:
        if c == '#':
            result[-1] += '#'
        else:
            result.append(c)
    if time == 0: 
        return result
    if len(result) >= time:
        return result[:time]
    result = result * (time // len(result)) + result[:time % len(result)]
    return result    

def checkSubArray(sub, arr):
    length = len(sub)
    print(sub, arr)
    for i in range(len(arr)):
        if sub == arr[i:i + length]:
            return True
    return False            

def solution(m, musicinfos):
    answer = "(None)"
    answerTime = 0
    for info in musicinfos:
        start, end, name, music = info.split(',')
        time = getTime(start, end)
        musicArr = getMusicArr(music, time)
        m = getMusicArr(m, 0)
        if checkSubArray(m, musicArr):
            if answerTime < time:
                answer = name
                answerTime = time
    return answer