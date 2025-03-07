lst = []
for _ in range(int(input())):
    cmd, *args = input().split()
    if cmd == "print":
        print(lst)
    else:
        getattr(lst, cmd)(*(map(int, args)))