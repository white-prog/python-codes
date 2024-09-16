def point_checker(s):
    pnt = 0
    for i in s:
        if i == "W":
            pnt += 3
        elif i == "D":
            pnt += 1
    return pnt

print(point_checker(['W','L','D','W','W']))