# Detecting if a point is in or out og the given square.

def IsPointSquare(x, y):
    return -1 <= x <= -0.5 and -0.5 <= y <= 0.5
    return -0.5 <= x <= 0.5 and -0.5 <= y <= 0.5
    return 0.5 <= x <= 1 and -0.5 <= y <= 0.5
    return -0.5 <= x <= 0.5 and -1 <= y <= -0.5
    return -0.5 <= x <= 0.5 and 0.5 <= y <= 1

x = float(input())
y = float(input())
if IsPointSquare(x, y):
    print('YES')
else:
    print('NO')