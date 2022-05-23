x, y, w, h = map(int, input().split())
way1 = x
way2 = y
way3 = w - x
way4 = h - y
ans = min(way1, way2, way3, way4)
print(ans)