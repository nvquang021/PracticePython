n = int(input())
arr = map(int, input().split())
score = list(arr)
score.sort(reverse = True)
for i in range(n):
    if score[i] < score[0]:
        print(score[i])
        break
    else:
        if score[i+1] < score[i]:
            print(score[i+1])
            break
    

    