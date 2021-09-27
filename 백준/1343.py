def makeString(type, count):
    if type == "X":
        if count % 2 != 0:
            return False
        return "AAAA" * (count // 4) + ("BB" if count % 4 != 0 else "")
    else:
        return "." * count


poly = input()
answer = ""
type = "X" if poly[0] == "X" else "."
cursor = 0
fail = False

while(cursor < len(poly)):
    count = 0
    while(cursor < len(poly)):
        if type == poly[cursor]:
            count += 1
            cursor += 1
        else:
            if makeString(type, count):
                answer += makeString(type, count)
            else:
                fail = True
            type = "." if poly[cursor] == "." else "X"
            break

if makeString(type, count):
    answer += makeString(type, count)
else:
    fail = True

if not fail:
    print(answer)
else:
    print(-1)
