from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
upper_length = len(belt) // 2
robot = deque([False] * upper_length)

answer = 0
while(k > 0):
    # 1단계
    belt.appendleft(belt.pop())
    robot.pop()
    robot.appendleft(False)
    # 로봇이 내리는 위치에 가면 바로 내리기
    if robot[-1] == True:
        robot[-1] = False
    # 2단계
    for i in range(len(robot) - 2, 0, -1):
        if belt[i + 1] != 0 and robot[i] == True and robot[i + 1] == False:
            robot[i], robot[i + 1] = robot[i + 1], robot[i]
            belt[i + 1] -= 1
            if belt[i + 1] == 0:
                k -= 1
            # 로봇이 내리는 위치면 바로 내리기
            if i == len(robot) - 2:
                robot[i + 1] = False
    # 3단계
    if belt[0] != 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            k -= 1
    answer += 1

print(answer)
