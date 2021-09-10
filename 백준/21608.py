n = int(input())
classroom = [[-1] * n for _ in range(n)]
students = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(n ** 2):
    students.append(list(map(int, input().split())))

# 1. 비어있는 칸 중 좋아하는 학생이 가장 많은 칸 찾기

# 2. 여러개면 인접한 칸 중 비어있는 칸이 많은 칸 선택

# 3. 위도 여러개면 행순 => 열 순으로 배치

# 4. 만족도 계산


def most_good_students_seat(student):
    # student_num = student[0]
    like_students = student[1:]
    most_adj_num = 0
    for x in range(n):
        for y in range(n):
            adj_num = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if classroom[nx][ny] in like_students:
                        adj_num += 1
            most_adj_num = max(most_adj_num, adj_num)


def most_empty_seat(seats):
    pass


def smallest_seat(seats):
    pass
