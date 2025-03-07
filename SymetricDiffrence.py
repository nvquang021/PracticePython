M = int(input()) 
set1 = set(map(int, input().split()))

N = int(input())
set2 = set(map(int, input().split())) 

symmetric_diff = set1 ^ set2  
for num in sorted(symmetric_diff):
    print(num)