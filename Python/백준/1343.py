poly = input()

poly = poly.replace("XXXX", "AAAA")
poly = poly.replace("XX", "BB")

print(-1) if 'X' in poly else print(poly)
