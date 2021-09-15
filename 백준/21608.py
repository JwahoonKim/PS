n = int(input())
classroom = [[-1] * n for _ in range(n)]
students = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n ** 2):
    students.append(list(map(int, input().split())))

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.


def most_good_students_seat(student):
    seats = []
    like_students = student[1:]
    most_adj_num = 0
    for x in range(n):
        for y in range(n):
            adj_num = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and classroom[x][y] == -1:
                    if classroom[nx][ny] in like_students:
                        adj_num += 1
            most_adj_num = max(most_adj_num, adj_num)

    for x in range(n):
        for y in range(n):
            adj_num = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in like_students and classroom[x][y] == -1:
                        adj_num += 1
            if adj_num == most_adj_num:
                if classroom[x][y] == -1:
                    seats.append((x, y))
    return seats

# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.


def most_empty_seat(seats, student):
    empty_seats = []
    most_empty_num = 0
    for x, y in seats:
        empty_num = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] == -1:
                    empty_num += 1
        most_empty_num = max(most_empty_num, empty_num)

    for x, y in seats:
        empty_num = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] == -1:
                    empty_num += 1
        if empty_num == most_empty_num:
            empty_seats.append((x, y))
    return empty_seats

# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.


def smallest_seat(seats):
    return sorted(seats)[0]

# student 정보가 들어오면 가장 적합한 자리를 찾아주기


def find_best_seat(student):
    seats = most_good_students_seat(student)
    seats = most_empty_seat(seats, student)
    return smallest_seat(seats)

# 만족도 계산


def count_satisfaction():
    satisfaction = 0
    score = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
    for x in range(n):
        for y in range(n):
            idx = 0
            adj_num = 0
            student = classroom[x][y]
            for i in range(len(students)):
                if students[i][0] == student:
                    idx = i
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in students[idx][1:]:
                        adj_num += 1
            satisfaction += score[adj_num]
    return satisfaction


# 학생들 자리배치하기
for student in students:
    x, y = find_best_seat(student)
    classroom[x][y] = student[0]

print(count_satisfaction())
