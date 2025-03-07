import math
a = int(input())
b = int(input())
if a < 0 or b < 0:
    print("Error")
else:
    text = "°"
    print(str(round(math.degrees(math.atan(a/b)))) + text)