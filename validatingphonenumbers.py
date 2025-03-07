n = int(input())
for _ in range(n):
    num = input()
    if num.isdigit() and len(num) == 10:
        if num[0] in ["7", "8", "9"]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")