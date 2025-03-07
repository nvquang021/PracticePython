# mn = [int(x) for x in input().split()]
# list1 = [int(x) for x in input().split()]
# A = [int(x) for x in input().split()]
# B = [int(x) for x in input().split()]
n, m = map(int, input().split())
arr = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((i in A) - (i in B) for i in arr))