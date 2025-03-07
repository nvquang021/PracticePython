n = int(input())
lst = set([int(x) for x in input().split()])

m = int(input())
for _ in range(m):
    cmd, *args = input().split()
    if cmd == "pop":
        if lst:
            lst.pop()
    elif cmd == "remove" and int(args[0]) in lst:
        lst.remove(int(args[0]))
    elif cmd == "discard" and int(args[0]) in lst:
        lst.discard(int(args[0]))
print(sum(lst))