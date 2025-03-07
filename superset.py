n = set(map(int, input().split()))
b = set(map(int, input().split()))
c = set(map(int, input().split()))
d = set(map(int, input().split()))

print(n.issuperset(b) and n.issuperset(c) and n.issuperset(d))