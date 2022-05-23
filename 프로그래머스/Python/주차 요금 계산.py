from collections import defaultdict
from math import ceil

def getTime(time):
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def calcFee(time, baseTime, baseFee, unitTime, unitFee):
    extraTime = max(0, time - baseTime)
    extraFee = ceil(extraTime / unitTime) * unitFee
    return baseFee + extraFee

def solution(fees, records):
    answer = []
    parkRecord = defaultdict(int)
    parkingLot = dict()
    baseTime, baseFee, unitTime, unitFee = fees

    for record in records:
        time, carNumber, type = record.split(' ')
        time = getTime(time)
        if type == "IN":
            parkingLot[carNumber] = time
        else:
            parkRecord[carNumber] += (time - parkingLot[carNumber])
            del parkingLot[carNumber]
    # 남은 차 처리
    for carNumber in parkingLot:
        parkRecord[carNumber] += (getTime("23:59") - parkingLot[carNumber])

    for carNumber in parkRecord:
        fee = calcFee(parkRecord[carNumber], baseTime, baseFee, unitTime, unitFee)
        answer.append([carNumber, fee])
    answer.sort()
    answer = [x[1] for x in answer]
    return answer
