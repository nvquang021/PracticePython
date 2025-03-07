string = str(input())
lower = []
upper = []
odd = []
even = []
for i in string:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif i.isdigit():
        if int(i) % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
print(''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even)))